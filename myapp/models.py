from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class loginModel(models.Model):
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=30)

class createModel(models.Model):
    img=CloudinaryField('image')
    title=models.CharField(max_length=80)
    description=models.CharField(max_length=250)
    author=models.CharField(max_length=20)

    
