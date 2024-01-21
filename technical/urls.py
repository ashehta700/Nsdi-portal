from django.urls import path , include
from technical import views






urlpatterns = [
    path('', views.view , name = "technical"),
    path('showmessage/', views.showMessage , name = "show-message"),
    path('showmessage/details/<int:message_id>', views.messageDetails , name = "message-details"),
    path('manual/', views.manual , name = "manual"),
    path('community/', views.community , name = "community"),
    path('community/comment-update/<int:comment_id>', views.update_comment , name = "update-comment"),
    path('community/comment-delete/<int:comment_id>', views.delete_comment , name = "delete-comment"),
    path('community/upload/', views.communityUpload , name = "create-question"),
    path('community/update/<int:question_id>', views.update_Question , name = "update-question"),
    path('community/delete/<int:question_id>', views.delete_question , name = "delete-question"),
    path('faq-center/', views.faqcenter , name = "faq-center"),
    path('faq-center/index', views.index , name = "index"),
    path('faq-center/upload/', views.upload, name = 'upload-problem'),
    path('faq-center/update/<int:problem_id>', views.update_problem),
    path('faq-center/delete/<int:problem_id>', views.delete_problem),
]