from django.contrib import admin
from cart.models import cart,Order,Account


# Register your models here.

admin.site.register(cart)
admin.site.register(Order)
admin.site.register(Account)