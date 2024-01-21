from django import forms
from .models import *






# form for extract Data   طلب استخراج البيانات 
class CreateExtract_data(forms.ModelForm):
    class Meta:
        model = Extract_data
        fields = '__all__'
        # exclude = ['response_date','refuse_date'] 





# form for mergeRequest طلب الدمج
class CreateMergeRequest(forms.ModelForm):
    class Meta:
        model = MergeRequest
        fields = '__all__'
        exclude = ['response_date','refuse_date','response_files','source_img','source_img_date','img_date','medany_date','medany_name','path'] 
        







# form for deploymentRequestlayer طلب نشر الطبقات
class CreatedeploymentRequestLayer(forms.ModelForm):
    class Meta:
        model = DeploymentRequest_layers
        fields = '__all__'
        exclude = ['response_date','refuse_date'] 



# form for InquiryRequest طلب إسنعلام
class CreateInquiryRequest(forms.ModelForm):
    class Meta:
        model = InquiryRequest
        fields = '__all__'
        exclude = ['response_date','refuse_date','url_sender']              
 # State
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['user_reciver'].queryset = self.fields['user_reciver'].queryset.exclude(role_id=3)
        self.fields['state'].queryset = State.objects.none()
        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
    
                self.fields['state'].queryset = State.objects.filter(
                    country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.country:

            self.fields['state'].queryset = self.instance.country.state_set.order_by(
                'name')

    # City
        
        self.fields['city'].queryset = City.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                
                self.fields['city'].queryset = City.objects.filter(
                    state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.state:
            
            self.fields['city'].queryset = self.instance.state.city_set.order_by(
                'name')
      



# form for deploymentRequestApp طلب نشر مؤشر الاداء
class CreatedeploymentRequestApp(forms.ModelForm):
    class Meta:
        model = DeploymentRequest_apps
        fields = '__all__'
        exclude = ['response_date','refuse_date']       
 # State
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].queryset = State.objects.none()
        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
    
                self.fields['state'].queryset = State.objects.filter(
                    country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.country:

            self.fields['state'].queryset = self.instance.country.state_set.order_by(
                'name')

    # City
        
        self.fields['city'].queryset = City.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                
                self.fields['city'].queryset = City.objects.filter(
                    state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.state:
            
            self.fields['city'].queryset = self.instance.state.city_set.order_by(
                'name')        




# form for deploymentRequestApp طلب نشر التطبيقات
class CreatedeploymentRequestApp2(forms.ModelForm):
    class Meta:
        model = DeploymentRequest_app2
        fields = '__all__'
        exclude = ['response_date','refuse_date']       
 # State
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].queryset = State.objects.none()
        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
    
                self.fields['state'].queryset = State.objects.filter(
                    country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.country:

            self.fields['state'].queryset = self.instance.country.state_set.order_by(
                'name')

    # City
        
        self.fields['city'].queryset = City.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                
                self.fields['city'].queryset = City.objects.filter(
                    state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.state:
            
            self.fields['city'].queryset = self.instance.state.city_set.order_by(
                'name')                   