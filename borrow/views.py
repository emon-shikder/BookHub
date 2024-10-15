from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from book.models import BookModel
from borrow.models import BookBorrowModel, BookReturnModel
from account.models import ProfileModel
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def order_email(user, amount, book, subject):
    """Send transactional email."""
    message = render_to_string(
        "borrow/order_email.html",
        {
            "user": user,
            "book": book,
            "amount": amount,
            "operation": subject,
        },
    )
    to_email = [user.email]
    send_email = EmailMultiAlternatives(subject=subject, body="", to=to_email)
    send_email.attach_alternative(message, "text/html")
    send_email.send()


def borrowView(request, id):
    """Borrow book view."""
    requested_book = get_object_or_404(BookModel, id=id)
    requested_user = ProfileModel.objects.get(user=request.user)

    if requested_book.book_quantity <= 0:
        messages.error(request, "This book is currently out of stock.")
        return redirect("book_detail", pk=id)

    if requested_user.balance < requested_book.book_price:
        messages.error(request, f"Insufficient balance. You need ${requested_book.book_price}.")
        return redirect("book_detail", pk=id)

    requested_book.book_quantity -= 1
    requested_book.save()

    requested_user.balance -= requested_book.book_price
    requested_user.save()

    order_email(
        request.user, requested_book.book_price, requested_book.book_name, "Borrow"
    )

    BookBorrowModel.objects.create(
        user=request.user,
        book=requested_book,
        status=True,
    )

    messages.success(request, f"Successfully borrowed '{requested_book.book_name}'.")
    return redirect("book_detail", pk=id)


def returnView(request, id):
    """Return book view."""
    requested_book = get_object_or_404(BookModel, id=id)
    requested_user = ProfileModel.objects.get(user=request.user)

    requested_book.book_quantity += 1
    requested_book.save()

    requested_user.balance += requested_book.book_price
    requested_user.save()

    order_email(
        request.user, requested_book.book_price, requested_book.book_name, "Return"
    )

    borrow_status = BookBorrowModel.objects.get(
        book=requested_book, user=request.user, status=True
    )
    borrow_status.status = False
    borrow_status.save()

    BookReturnModel.objects.create(
        user=request.user,
        book=requested_book,
        status=True,
    )

    messages.success(request, f"Successfully returned '{requested_book.book_name}'.")
    return redirect("book_detail", pk=id)
