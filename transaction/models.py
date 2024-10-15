from django.db import models
from django.contrib.auth.models import User
from transaction.constants import TRANSACTION_TYPE
# Create your models here.


class TransactionModel(models.Model):
    transaction_time = models.DateTimeField(auto_now_add=True)
    transaction_amount = models.IntegerField()
    transaction_type=models.CharField(choices=TRANSACTION_TYPE,max_length=400)
    after_transaction_balance = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
