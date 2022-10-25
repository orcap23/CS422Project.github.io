from django.urls import re_path, path
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


# namespace
app_name = "file_upload"


#re_path is a callable within the django. urls module of the Django project.
#Django URL pass parameter to view You can pass a URL parameter from the URL to a view using a path converter. 
urlpatterns = [
    # Upload File 
    re_path(r'^upload/$', views.file_upload, name='file_upload'),
    # View File List
    path('', views.file_list, name='file_list'),
    path('delete_file/<int:pk>', views.delete_file, name="delete_file"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)