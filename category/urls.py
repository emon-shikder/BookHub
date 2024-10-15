from django.urls import path
from .views import CategoriesBookView

urlpatterns = [
    path('category/<path:category_name>/', CategoriesBookView, name='books_by_category'),
]
