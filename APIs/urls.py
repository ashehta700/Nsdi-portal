from django.urls import path
from APIs import views

urlpatterns = [
    path('data/', views.my_query,name="zoomTo"), # return row depend on x and y paramater 
    path('csv/', views.response_csv,name='downloadCsv'), # return all data depend on polygon 
    path('send_data/', views.Send_Data,name="Send_Data"), # send request post to basemap
    path('export_csv/', views.export_csv,name="export_csv"), # get all data from merge app depend on user_id
    path('check_serag/', views.check_serag,name="check_serag"), # get all data from merge app depend on user_id
    path('inquiry/',views.inquiry,name="inquiry"),
    path('merge/',views.MergeApp,name="merge_app"),
]