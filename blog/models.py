from django.db import models
class comment (models.Model):
    name = models.CharField(max_length=20 , null=True)
    comment = models.CharField(null=True)
    ip =models.GenericIPAddressField(null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment
class message (models.Model):
    username= models.CharField(max_length=20 , null=True)
    email = models.EmailField(null=True)
    message =models.TextField(null=True)
class posts (models.Model):
    head =models.CharField(max_length=20 , null=True)
    image=models.ImageField( upload_to='photos\%y\%m\%d', null=True)
    deatil =models.TextField(null=True)
# Create your models here.
