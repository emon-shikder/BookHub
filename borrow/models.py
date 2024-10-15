from django.db import models
from django.contrib.auth.models import User
from book.models import BookModel
# Create your models here.

class BookBorrowModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE)
    borrow_time=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)

class BookReturnModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE)
    return_time=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)
    