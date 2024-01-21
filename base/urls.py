from django.urls import path , include
from base import views






urlpatterns = [
    
    path('', views.view , name = "base"),
    path('login/', views.login , name = "login"),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register , name = "register"),
    path('update-user/<int:profiles_id>', views.updateProfiles , name = "update-user"), # update profile for user
    path('users/index/', views.ListUsers, name='ListUsers'), # reset password for user
    path('users/index/update/<int:user_id>', views.UpdateUser, name='updateUser'), # update user form admin panel
    path('users/index/delete/<int:user_id>', views.deleteUser, name='deleteUser'), # delete user form admin panel
    path('apps/', views.apps , name = "apps"),
    path('cat_apps/', views.cat_apps , name = "cat_apps"),
    path('cat_apps/catList/<int:id>', views.cat_apps_sub , name = "categoryAPPSub"),
    path('cat_apps/catList-sub/<int:id>', views.cat_sub , name = "catSub"),
    path('apps/index', views.appsIndex , name = "apps-index"),
    path('apps/index/create', views.appsCreate , name = "apps-create"),
    path('apps/index/update/<int:app_id>', views.updateApp , name = "apps-update"),
    path('apps/index/delete/<int:app_id>', views.deleteApp , name = "apps-delete"),


] 