from django.db import models

class userpayments(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=25)
    phone = models.IntegerField(null=False)
    cart = models.BooleanField(default=False)
    wishlist = models.BooleanField(default=False)
    product_name = models.CharField(max_length=999)
    address = models.CharField(max_length=999)
    product_category = models.CharField(max_length=999)
    product_id = models.IntegerField()
    available = models.IntegerField()
    price = models.IntegerField()
    tax = models.IntegerField()
    discount = models.IntegerField()
    quantity = models.IntegerField(default=1)
    paymentid = models.CharField(max_length=99,default="False")
    paymentstatus = models.BooleanField(default=False)
 