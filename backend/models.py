from django.db import models

class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=128)

class News(models.Model):
    title = models.CharField(max_length=64)
    desc = models.TextField()

class Product(models.Model):
    title = models.CharField(max_length=64)
    desc = models.TextField()

class Option(models.Model):
    title = models.CharField(max_length=64)
    desc = models.TextField()
