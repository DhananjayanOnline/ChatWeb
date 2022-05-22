from django.db import models

# Create your models here.

class Registration(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
