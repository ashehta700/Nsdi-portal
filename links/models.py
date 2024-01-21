from django.db import models
from datetime import datetime
from base .models import *

# Create your models here.

class News(models.Model):
    title = models.TextField()
    description = models.TextField()
    photo = models.FileField(default='news/default.png' ,upload_to='news', null=True , blank=True)
    video = models.FileField(upload_to='news/videos', null=True , blank=True)
    youtube_link = models.CharField(max_length=200,null=True, blank=True)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    news_view = models.IntegerField(default=0)

    def get_date(self):
        time = datetime.now()
        if self.date.day == time.day:
            if time.hour == (self.date.hour+2):
                return " منذ " + str(time.minute - self.date.minute) + " دقائق "
            else:
                return " منذ " + str(time.hour - (self.date.hour+2)) + " ساعات "                       
        else:
            if self.date.month == time.month:
                return " منذ " + str(time.day - self.date.day) + " ايام "
            else:
                if self.date.year == time.year:
                    return " منذ " + str(time.month - self.date.month) + " اشهر "
        return self.date
    

    def __str__(self):
        return self.title









class Apps(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(default='apps/default.jpg' ,upload_to='apps/', null=True , blank=True)
    link = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    organization_name = models.ForeignKey(Gehat, on_delete=models.CASCADE ,null=True)
    Apps_category_Sub = models.ForeignKey('Apps_category_Sub' , on_delete=models.CASCADE ,null=True)


    def __str__(self):
        return self.name


class Apps_category_Sub(models.Model):
    catoName = models.CharField(max_length= 100)
    image = models.FileField(default='apps/default.jpg' ,upload_to='apps/', null=True , blank=True)
    Apps_category = models.ForeignKey('Apps_category' , on_delete=models.CASCADE ,null=True) 
    def __str__(self):
        return self.catoName



class Apps_category(models.Model):
    catoName = models.CharField(max_length= 100)
    image = models.FileField(default='apps/default.jpg' ,upload_to='apps/', null=True , blank=True)

    def __str__(self):
        return self.catoName
    