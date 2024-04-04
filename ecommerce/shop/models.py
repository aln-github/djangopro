from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='catmed/image',null=True,blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='products', null=True, blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True) # date and time add one time
    updated = models.DateTimeField(auto_now=True) # date and time every time we update records
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name







