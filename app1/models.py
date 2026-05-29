from django.db import models

# Create your models here.
class student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=20)
    age=models.IntegerField()
    course=models.CharField(max_length=20)


    
