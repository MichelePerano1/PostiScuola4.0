from django.db import models
from django.db.models.functions import Now



# Create your models here.

class ModelloPosti(models.Model):
    posto1=models.CharField(max_length=30)
    posto2=models.CharField(max_length=30)
    posto3=models.CharField(max_length=30)
    posto4=models.CharField(max_length=30)
    posto5=models.CharField(max_length=30)
    posto6=models.CharField(max_length=30)
    posto7=models.CharField(max_length=30)
    posto8=models.CharField(max_length=30)
    posto9=models.CharField(max_length=30)
    posto10=models.CharField(max_length=30)
    posto11=models.CharField(max_length=30)
    posto12=models.CharField(max_length=30)
    posto13=models.CharField(max_length=30)
    posto14=models.CharField(max_length=30)
    posto15=models.CharField(max_length=30)
    posto16=models.CharField(max_length=30)
    posto17=models.CharField(max_length=30)
    posto18=models.CharField(max_length=30)
    posto19=models.CharField(max_length=30)
    posto20=models.CharField(max_length=30)
    posto21=models.CharField(max_length=30)
    posto22=models.CharField(max_length=30,blank=True)

    data=models.DateField(auto_now_add=True)
