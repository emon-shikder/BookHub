from django.shortcuts import render
from django.views.generic import DetailView
from book.models import BookModel
from borrow.models import BookBorrowModel
from review.forms import ReviewForm

# Create your views here.


class BookDetailPageView(DetailView):
    model = BookModel
    template_name = "book/book_details.html"
    pk_url_kwarg = "pk"
    context_object_name = "book_details"

    def post(self, request, *args, **kwargs):
        review_form = ReviewForm(data=self.request.POST)
        requested_book = self.get_object()
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.user = request.user
            new_review.book = requested_book
            new_review.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        if self.request.user.is_authenticated:
            user = self.request.user
            flag = BookBorrowModel.objects.filter(
                user=user,
                book=book,
                status=True,
            ).exists()
            context["flag"] = flag
        reviews = book.review.all()
        context["reviews"] = reviews
        context["ReviewForm"] = ReviewForm()
        return context
