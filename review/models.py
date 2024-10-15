from django.db import models
from django.contrib.auth.models import User
from book.models import BookModel

# Create your models here.


class ReviewModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE,related_name='review',default=None)
    review_creation_time = models.DateTimeField(auto_now_add=True)
    reveiw_body = models.TextField()
