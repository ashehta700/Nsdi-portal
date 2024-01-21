from django import forms
from .models import *


class ProblemsCreate(forms.ModelForm):
    class Meta:
        model = Problems
        fields = '__all__'


class CommunityCreate(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['profile_id','date'] 



class AnswerCreate(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ['profile_id','date','question_id'] 
        


class ContactUsCreate(forms.ModelForm):
    class Meta : 
        model = ContactUs
        exclude = ['profile_id','phone','address'] 

        