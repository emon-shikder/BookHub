from django.urls import path, include
from core.views import HomePageView, categories_view

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("account/", include("account.urls")),
    path("book/", include("book.urls")),
    path("borrow/", include("borrow.urls")),
    path("category/", include("category.urls")),
    path('categories/', categories_view, name='categories'),
    path("review/", include("review.urls")),
    path("transaction/", include("transaction.urls")),
]
