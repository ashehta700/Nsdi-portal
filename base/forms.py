from django import forms
from base.models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class ExtendedUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

    def save(self,commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user        


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profiles 
        fields = ['name','phone','organization_address','organization_name','image','user_job','role_id','user_role','tenant_link']   

