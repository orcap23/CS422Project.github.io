from django.db import models
import os
import uuid


def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    


class File(models.Model):
    upload_method = models.CharField(max_length=20, verbose_name="User Name")
    file = models.FileField(upload_to=user_directory_path, null=True)

