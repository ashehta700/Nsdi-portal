from django.urls import path , include
from links import views





urlpatterns = [
    path('wezarat/', views.Wezarat , name = "wezarat"),
    path('mohafazat/', views.mohafazat , name = "mohafazat"),
    path('he2at/', views.he2at , name = "he2at"),
    path('cat/', views.showCategories , name = "cat_tap"),
    path('catList/<int:cat_id>', views.showCategories_sub , name = "categorySub"),
    path('cat/<int:cat_id>', views.categoryList , name = "categoryList"),
    path('allDash/', views.allDash , name = "allDash"),
    path('allDash/load/', views.loadMore , name = "load"),
    path('taps/index', views.listTaps , name = "listTaps"),
    path('taps/index/create', views.addTap , name = "addTap"),
    path('taps/index/update/<int:tap_id>', views.updateTap , name = "updateTap"),
    path('taps/index/delete/<int:tap_id>', views.deleteTap , name = "deleteTap"),
    path('addUserLinks/', views.addUserLinks , name = "addUserLinks"),
    path('news/index', views.index , name = "news-index"),
    path('news/index/details/<int:news_id>', views.details , name = "news-details"),
    path('news/createNews', views.createNewss , name = "createNews"),
    path('news/newscontrol', views.newscontrol , name = "newscontrol"),
    path('news/newscontrol/update/<int:news_id>', views.updateNews , name = "updateNews"),
    path('news/newscontrol/delete/<int:news_id>', views.delete_news , name = "updateNews"),


] 