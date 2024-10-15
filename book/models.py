from django.db import models
from category.models import CategoryModel

# Create your models here.


class BookModel(models.Model):
    book_image = models.ImageField(upload_to="book/media/upload")
    book_name = models.CharField(max_length=800)
    book_title = models.CharField(max_length=800)
    book_description = models.TextField()
    book_publisher = models.CharField(max_length=800)
    book_edision = models.CharField(max_length=800)
    number_of_pages = models.IntegerField()
    book_language = models.CharField(max_length=800)
    book_origin = models.CharField(max_length=800)
    book_price=models.IntegerField(default=0)
    book_quantity=models.IntegerField(default=5)
    book_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book_name}"
