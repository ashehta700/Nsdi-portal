from django.db import models
from django.db.models.signals import *
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


# Create your models here.








class Gehat(models.Model):
    name = models.CharField(max_length=200) 

    def __str__(self):
        return self.name 




class Roles(models.Model):
    name = models.CharField(max_length= 250)
    code = models.IntegerField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name




#  roles for 3 permission of users 
class user_roles(models.Model):
    name = models.CharField(max_length= 250)
    code = models.IntegerField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name        





class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='Profiles',null=True,unique=False)
    name = models.CharField(max_length = 100 , null=True)
    phone = models.CharField(max_length = 100 , null=True)
    organization_address = models.CharField(max_length = 150 , null=True)
    organization_name = models.ForeignKey(Gehat, on_delete=models.CASCADE ,null=True)
    user_job = models.CharField(max_length = 150 , null=True)
    image= models.FileField(default='already.png' ,upload_to='profiles', null=True , blank=True)
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE,null=True )
    user_role = models.ForeignKey(user_roles, on_delete=models.CASCADE,null=True )
    tenant_link = models.CharField(max_length = 150 , null=True)


    
    
    def __str__(self):
        return self.name


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs['created']:
        user_profile = Profiles(user=user)
post_save.connect(create_profile,sender=User)



    # to customize image when uploaded to the fixed size 
    # def save(self , *args , **kwargs):
    #     imgage = Image.open(self.image.path)
    #     if imgage.height >300 or imgage.width > 300 :
    #         output_size = (300,300)
    #         imgage.thumbnail(output_size)
    #         imgage.save(self.image.path)
       
# taps_category
class taps_categories(models.Model):
    name = models.CharField(max_length=100)
    icon_path= models.CharField(max_length=150,null=True)


   
    def __str__(self):
        return self.name




# taps_category_sub
class taps_categories_sub(models.Model):
    name = models.CharField(max_length=100)
    tabs_category_id = models.ForeignKey(taps_categories,on_delete=models.CASCADE,null=False)
    icon_path= models.CharField(max_length=150,null=True)

   
    def __str__(self):
        return self.name        




class Taps(models.Model):
    tap_name = models.CharField(max_length=100)
    tap_description=models.TextField(max_length=255 , null=True)
    tap_link = models.CharField(max_length=255)
    gehat_id = models.ForeignKey(Gehat, on_delete=models.CASCADE ,null=True)
    taps_categories_sub_id = models.ForeignKey(
        taps_categories_sub, blank=True, on_delete=models.SET_NULL ,null=True )
   
    def __str__(self):
        return self.tap_name



class User_links(models.Model):
    user_id = models.ForeignKey(Profiles, on_delete=models.CASCADE , null=True)
    tap_id = models.ForeignKey(Taps, on_delete=models.CASCADE , null=True) 

    def __str__(self):
        return str(self.user_id)



     

