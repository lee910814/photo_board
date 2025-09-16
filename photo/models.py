from django.db import models

# Create your models here.

class Photo(models.Model):
    title : models.CharField(max_length=150)
    image : models.CharField(max_length=200)
    description : models.TextField() # type: ignore
