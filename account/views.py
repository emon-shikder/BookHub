from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from account.forms import UserSignUpForm, CustomAuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView
from borrow.models import BookBorrowModel, BookReturnModel
from transaction.models import TransactionModel
from review.models import ReviewModel

# Create your views here.


class UserSignUpPageView(FormView):
    form_class = UserSignUpForm
    template_name = "account/sign_up.html"

    def get_success_url(self):
        return reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserLoginPageView(LoginView):
    template_name = "account/login.html"
    authentication_form = CustomAuthenticationForm

    def get_success_url(self):
        return reverse_lazy("home")


class UserLogoutView(LogoutView):
    def get_success_url(self):
        logout(self.request)
        return reverse_lazy("home")


def ProfilePageView(request, profilenav):
    if profilenav == "account":
        context = {
            "flag": "account",
        }
        return render(request, "account/profile.html", context)
    elif profilenav == "borrow":
        borrowed_books = BookBorrowModel.objects.filter(user=request.user)
        context = {
            "borrowed_books": borrowed_books,
            "flag": "borrow",
        }
        return render(request, "account/profile.html", context)
    elif profilenav == "return":
        returned_books = BookReturnModel.objects.filter(user=request.user)
        context = {
            "returned_books": returned_books,
            "flag": "return",
        }
        return render(request, "account/profile.html", context)
    elif profilenav == "transactions":
        transactions = TransactionModel.objects.filter(user=request.user)
        context = {
            "transactions": transactions,
            "flag": "transactions",
        }
        return render(request, "account/profile.html", context)
    elif profilenav == "reviews":
        reviews = ReviewModel.objects.filter(user=request.user)
        context = {
            "reviews": reviews,
            "flag": "reviews",
        }
        return render(request, "account/profile.html", context)
