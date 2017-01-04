from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    resume=models.TextField()
    price=models.IntegerField()