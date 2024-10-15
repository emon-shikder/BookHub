from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    category_name=models.CharField(max_length=800)
    slug=models.SlugField(max_length=1000,unique=True)
    
    def __str__(self):
        return f"{self.category_name}"