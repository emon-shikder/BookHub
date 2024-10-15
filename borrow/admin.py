from django.contrib import admin
from borrow.models import BookBorrowModel,BookReturnModel
# Register your models here.

admin.site.register(BookBorrowModel)
admin.site.register(BookReturnModel)