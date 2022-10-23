from django.urls import path,re_path
from . import views


urlpatterns = [
    path('', views.say_sth),
    path('download/', views.downloadtrainset),
    #path('link/', views.linkto_detail),
    re_path(r'^upload/$', views.file_upload),
    path('filelist/', views.file_list),
 
]