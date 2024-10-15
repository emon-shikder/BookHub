from django.shortcuts import render, get_object_or_404
from category.models import CategoryModel
from book.models import BookModel

def CategoriesBookView(request, category_name):
    category = get_object_or_404(CategoryModel, category_name=category_name)
    
    books = BookModel.objects.filter(book_category=category)
    
    context = {
        "books": books,
        "category_name": category.category_name,
    }
    
    return render(request, "category/books_by_category.html", context)
