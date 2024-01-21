from django.urls import path , include
from admin_panel import views





urlpatterns = [
    path('', views.index , name="admin_panel_index"),
]
