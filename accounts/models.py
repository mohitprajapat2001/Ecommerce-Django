from django.db import models

# Create your models here.
class user(models.Model):
    GENDER = (
        ('M','M'), #Male
        ('F','F') #Female
    )
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=25)
    phone = models.IntegerField()
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    dob = models.DateTimeField()
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    profession = models.CharField(max_length=30)
    status = models.CharField(max_length=30)