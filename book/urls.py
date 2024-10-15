from django.urls import path, include
from book.views import BookDetailPageView
urlpatterns = [
    path('book-detail/<int:pk>/',BookDetailPageView.as_view(),name='book_detail')
]