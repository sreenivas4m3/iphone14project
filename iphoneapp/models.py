from django.db import models


# Create your models here.
class iphone14(models.Model):
      name=models.TextField(default="")
      version=models.TextField(default="")
      maincamera=models.TextField(default="")
      rearcamera=models.TextField(default="")
      battery=models.TextField(default="")
      display=models.TextField(default="")
      memory=models.TextField(default="")


