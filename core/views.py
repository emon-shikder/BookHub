from django.shortcuts import render
from django.views.generic import ListView
from category.models import CategoryModel
from book.models import BookModel

class HomePageView(ListView):
    template_name = "core/index.html"
    model = BookModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = CategoryModel.objects.all()
        context["all_books"] = BookModel.objects.all()  # Fetch all books
        return context

from category.models import CategoryModel

def categories_view(request):
    categories = CategoryModel.objects.all()  # Fetch all categories
    return render(request, 'core/categories.html', {'categories': categories})