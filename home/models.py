from django.db import models

# Create your models here.
class products(models.Model):    
    PRODUCT_CATEGORY = (
        ('groseries', 'Groseries'),
        ('home', 'Home Decor'),
        ('mobile', 'Phone'),
        ('fashion', 'Fashion'),
        ('O', 'Other'),)
    image1 = models.ImageField(upload_to='productimg')
    image2 = models.ImageField(upload_to='productimg')
    image3 = models.ImageField(upload_to='productimg')
    image4 = models.ImageField(upload_to='productimg')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    tax = models.IntegerField()
    size = models.CharField(max_length=20)
    description = models.TextField()
    category = models.CharField(max_length=25,choices=PRODUCT_CATEGORY)
    available = models.IntegerField()
    offer = models.BooleanField(default=True)
    discount = models.IntegerField()
    def __str__(self):
        return self.name  
    

class carasouelimage(models.Model):
    images = models.ImageField(upload_to='carasouel_image')
    show = models.BooleanField(default=True)