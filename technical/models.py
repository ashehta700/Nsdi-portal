from django.db import models
from datetime import datetime
from base .models import *

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Problems(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.TextField(max_length=255)
    answer = models.TextField(max_length=255)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.question



class Question(models.Model):
    name = models.TextField(max_length=255)
    date = models.DateTimeField(default=datetime.now, blank=True , null=True)
    profile_id = models.ForeignKey(Profiles, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        ordering = ['-date']

      


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.TextField(max_length=255)
    date = models.DateTimeField(default=datetime.now, blank=True)
    profile_id = models.ForeignKey(Profiles, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        ordering = ['-date']




class ContactUs(models.Model):
    profile_id = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    phone = models.TextField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=100)
    message = models.TextField(max_length=255)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.profile_id.name       

          
