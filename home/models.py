from django.db import models

# Create your models here.
class products(models.Model):
    image1 = models.ImageField(upload_to='productimg')
    image2 = models.ImageField(upload_to='productimg')
    image3 = models.ImageField(upload_to='productimg')
    image4 = models.ImageField(upload_to='productimg')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    tax = models.IntegerField()
    size = models.CharField(max_length=20)
    description = models.TextField()
    category = models.CharField(max_length=50)
    available = models.IntegerField()
    offer = models.BooleanField(default=True)
    discount = models.IntegerField()
    

class carasouelimage(models.Model):
    images = models.ImageField(upload_to='carasouel_image')
    show = models.BooleanField(default=True)