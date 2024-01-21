from django.db import models
from base .models import *
from datetime import datetime

# Create your models here.

# model for MergeRequest طلب الدمج    

class MergeRequest(models.Model):
    user_sender = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    files = models.FileField(upload_to='mergeRequest/', null=True , blank=True)
    path = models.CharField(max_length=255)
    note = models.TextField()
    response_date = models.DateTimeField(default=datetime.now,null=True, blank=True)
    response_message = models.TextField(null=True,blank=True)
    # response_files = models.FileField(upload_to='mergeRequest/response', null=True , blank=True)
    refuse_date = models.DateTimeField(default=datetime.now,null=True, blank=True)
    refuse_message = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.user_sender)






# طلب استخراج البيانات
class Extract_data(models.Model):
    user_sender = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    path = models.CharField(max_length=255)
    note = models.TextField()
    response_date = models.DateTimeField(null=True, blank=True)
    response_message = models.TextField(null=True,blank=True)
    response_files = models.FileField(upload_to='Extract_data/', null=True , blank=True)
    refuse_date = models.DateTimeField(null=True, blank=True)
    refuse_message = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.user_sender)


      

# طلبات نشر الطبقات 
class DeploymentRequest_layers(models.Model):
    user_sender = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    layer_link = models.CharField(max_length=200,null=True)
    layer_name = models.CharField(max_length=150,null=True)
    LAYER_TYPE = (
    ('Point', 'Point'),
    ('Line', 'Line'),
    ('Polygon', 'Polygon'),)
    layer_type = models.CharField(max_length=150,choices=LAYER_TYPE,null=True)
    SERVICE_TYPE = (
    ('WMS', 'WMS'),
    ('WFS', 'WFS'),
    ('ALL', 'ALL'),)
    service_type = models.CharField(max_length=150,choices=SERVICE_TYPE,null=True)
    PUBLISH_TYPE = (
    ('لجميع الجهات', 'لجميع الجهات'),
    ('خاص بالجهه فقط', 'خاص بالجهه فقط'),)
    publish_type = models.CharField(max_length=255,choices=PUBLISH_TYPE,default="لجميع الجهات")
    image = models.FileField(upload_to='deploymentRequest/', null=True , blank=True) # image for layer
    layer_description = models.TextField()
    # 
    # --------------meta data -------------------
    FILE_TYPE = (
    ('Shape File', 'Shape File'),
    ('Geo DataBase', 'Geo DataBase'),
    ('Cad File', 'Cad File'),
    ('Excel File', 'Excel File'),)
    file_type = models.CharField(max_length=150,choices=FILE_TYPE,null=True) #نوع الملف 
    PROJ_TYPE = (
    ('UTM', 'UTM'),
    ('ETM', 'ETM'),)
    entry_proj  = models.CharField(max_length=150,choices=PROJ_TYPE,null=True) #الاسقاط
    # 
    source_img  = models.CharField(max_length=150,null=True) #مصدر الصورة
    source_img_date  =  models.DateTimeField(default=datetime.now, blank=True) #تاريخ انشاء البيانات الهندسية  
    img_date  =  models.DateTimeField(default=datetime.now, blank=True) #تاريخ الصورة  
    # 
    medany_date =  models.DateTimeField(default=datetime.now, blank=True)    #تاريخ الرفع الميدانى   
    medany_name =   models.CharField(max_length=150,null=True)    #اسم الجهه القائمة بالرفع الميدانى 
    # 
    db_entry_name =   models.CharField(max_length=150,blank=True)  #اسم المسؤؤل عن نشر الطبقة 
    db_entry_id =   models.CharField(max_length=100,null=True) #الرقم القومي لمدخل البيانات 
    # 
    wasf_source = models.CharField(max_length=150,null=True)  # مصدر البيانات الوصفية
    wasf_address = models.CharField(max_length=150,null=True)  # عنوان البيانات الوصفية 
    wasf_date = models.CharField(max_length=150,null=True)  #تاريخ التعامل مع البيانات الوصفية
    # 
    response_date = models.DateTimeField(default=datetime.now,null=True, blank=True)
    response_message = models.TextField(null=True,blank=True)
    refuse_date = models.DateTimeField(default=datetime.now,null=True, blank=True)
    refuse_message = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.user_sender) 




class Country(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]


class State(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    country = models.ForeignKey(
        'Country', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]


class City(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    state = models.ForeignKey(
        'State', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["-name"]



# طلب الاستعلام
class InquiryRequest(models.Model):
    user_sender = models.ForeignKey(Profiles,related_name="user_sender", on_delete=models.CASCADE)
    user_reciver = models.ForeignKey(Gehat,related_name="user_reciver", on_delete=models.CASCADE)
    request_date = models.DateTimeField(default=datetime.now,null=True, blank=True)
    request_message = models.TextField()
    url_sender = models.CharField(max_length=255)
    files = models.FileField(upload_to='inquiryRequest/', null=True , blank=True)
    coor_lat = models.CharField(max_length=255,null=True,blank=True)
    coor_lon = models.CharField(max_length=255,null=True,blank=True)
    country = models.ForeignKey(
        "Country", on_delete=models.SET_NULL, blank=True ,null=True )
    state = models.ForeignKey(
        'State', blank=True, on_delete=models.SET_NULL ,null=True )
    city = models.ForeignKey(
        "City", on_delete=models.SET_NULL, blank=True , null=True)
    response_message = models.TextField( null=True, blank=True)
    response_date =  models.DateTimeField(default=datetime.now,null=True, blank=True)
    response_url = models.CharField(max_length=255,null=True,blank=True)
    response_file = models.FileField(upload_to='inquiryRequest/', null=True , blank=True)
    refuse_message = models.TextField( null=True, blank=True)
    refuse_date =  models.DateTimeField(default=datetime.now,null=True, blank=True)
    refuse_admin_message = models.TextField( null=True, blank=True)  # refuse from admin before going to user_reciver 
    refuse_admin_date =  models.DateTimeField(default=datetime.now,null=True, blank=True) # refuse from admin before going to user_reciver
    is_approved = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.user_sender) 


# model for MergeRequest مؤشر الداء طلب النشر    

class DeploymentRequest_apps(models.Model):
    user_sender = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    app_link = models.CharField(max_length=255)
    app_description = models.TextField()
    response_date = models.DateTimeField(default=datetime.now,null=True, blank=True)
    response_message = models.TextField(null=True,blank=True)
    refuse_date = models.DateTimeField(default=datetime.now,null=True, blank=True)
    refuse_message = models.TextField(null=True,blank=True)
    country = models.ForeignKey(
        "Country", on_delete=models.SET_NULL, blank=True ,null=True )
    state = models.ForeignKey(
        'State', blank=True, on_delete=models.SET_NULL ,null=True )
    city = models.ForeignKey(
        "City", on_delete=models.SET_NULL, blank=True , null=True)



    def __str__(self):
        return str(self.user_sender)  
        




class DeploymentRequest_app2(models.Model):
    user_sender = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    app_link = models.CharField(max_length=255)
    app_description = models.TextField()
    response_date = models.DateTimeField(default=datetime.now,null=True, blank=True)
    response_message = models.TextField(null=True,blank=True)
    refuse_date = models.DateTimeField(default=datetime.now,null=True, blank=True)
    refuse_message = models.TextField(null=True,blank=True)
    country = models.ForeignKey(
        "Country", on_delete=models.SET_NULL, blank=True ,null=True )
    state = models.ForeignKey(
        'State', blank=True, on_delete=models.SET_NULL ,null=True )
    city = models.ForeignKey(
        "City", on_delete=models.SET_NULL, blank=True , null=True)



    def __str__(self):
        return str(self.user_sender)  
        
        