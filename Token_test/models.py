from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Book(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    author= models.CharField(max_length=50)
