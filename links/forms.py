from django import forms
from .models import *
from base .models import *



class TapCreate(forms.ModelForm):
    class Meta:
        model = Taps
        fields = '__all__'


      



class UserLinksCreate(forms.ModelForm):
    class Meta:
        model = User_links
        fields = '__all__'            


class createNews(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__' 
        exclude = ['news_view'] 


class createApp(forms.ModelForm):
    class Meta:
        model = Apps
        fields = '__all__' 
        exclude = ['date']        
         
        