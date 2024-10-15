from django.db import models
from django.contrib.auth.models import User
from account.constants import GENDER_TYPE

# Create your models here.


class ProfileModel(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile_info"
    )
    gender = models.CharField(max_length=250, choices=GENDER_TYPE)
    balance = models.IntegerField(default=0)
    birth_date = models.DateField()
    city = models.CharField(max_length=350)
    street = models.CharField(max_length=750)
    country = models.CharField(max_length=800)
    post_code = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.user.username}"
    
