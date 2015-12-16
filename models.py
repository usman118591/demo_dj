from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Articles(models.Model):
    tite=models.TextField(max_length=250)
    body=models.TextField(max_length=250)
    
class Comment(models.Model):
    article=models.ForeignKey(Articles)
    text=models.TextField()
    