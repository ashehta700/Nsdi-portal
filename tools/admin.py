from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(MergeRequest)
admin.site.register(DeploymentRequest_apps)
admin.site.register(DeploymentRequest_layers)
admin.site.register(InquiryRequest)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)