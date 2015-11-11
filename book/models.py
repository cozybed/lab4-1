from django.db import models

# Create your models here.
class author(models.Model):
    authorID = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    country = models.CharField(max_length=30)


class books(models.Model):
    ISBN = models.CharField(max_length=30, primary_key=True)
    Title = models.CharField(max_length=40)
    author = models.CharField(max_length=30)
    publisher = models.CharField(max_length=30)
    publishDate = models.DateField()
    price = models.IntegerField()
