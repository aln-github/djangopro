from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
# Create your models here.

class cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    data_added=models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        return self.quantity*self.product.price

    def __str__(self):
        return self.product.name

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    no_items=models.IntegerField()
    phone=models.BigIntegerField()
    address=models.TextField()
    ordered_date=models.DateTimeField(auto_now_add=True)
    ordered_status=models.CharField(max_length=30,default="pending")
    delivery_status=models.CharField(max_length=30,default="pending")

    def __str__(self):
        return self.user.username




class Account(models.Model):
    acc_no=models.BigIntegerField()
    acc_type=models.CharField(max_length=20)
    amount=models.IntegerField()

    def __str__(self):
        return str(self.acc_no)
