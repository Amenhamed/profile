from django.db import models
from django.contrib.auth.models import User
class comment (models.Model):
    name = models.CharField(max_length=50)  # اسم الزائر
    comment = models.CharField(max_length=500)  # نص التعليق (حد أقصى 500 حرف مثلاً)
    session_id = models.CharField(max_length=40)  # معرّف الزائر
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}: {self.comment[:20]}"
class message (models.Model):
    username= models.CharField(max_length=20 , null=True)
    email = models.EmailField(null=True)
    message =models.TextField(null=True)
class posts (models.Model):
    head =models.CharField(max_length=20 , null=True)
    image=models.ImageField( upload_to='photos/%y/%m/%d', null=True)
    deatil =models.TextField(null=True)
# Create your models here.
