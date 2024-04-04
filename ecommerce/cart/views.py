from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from shop.models import Product
from cart.models import cart,Account,Order

# Create your views here.

@login_required
# for displaying the cart for current user
def cart_view(request):
    u=request.user
    c=cart.objects.filter(user=u)
    total=0
    for i in c:
        total=total+i.quantity*i.product.price
    return render(request,'cart.html',{'c':c,'total':total})

@login_required
# for adding particular product to cart table
def addtocart(request,p):
    p=Product.objects.get(id=p)
    u=request.user
    try:
        Cart=cart.objects.get(user=u,product=p)
        if p.stock>0:
            Cart.quantity += 1
            Cart.save()
            p.stock -=1
            p.save()

    except:
        if p.stock>0:
            Cart = cart.objects.create(product=p, user=u, quantity=1)
            Cart.save()
            p.stock -=1
            p.save

    return cart_view(request)


def cart_decrement(request,p):
    p = Product.objects.get(id=p)
    u = request.user
    try:
        Cart = cart.objects.get(user=u, product=p)
        if(Cart.quantity>1):

            Cart.quantity -=1
            Cart.save()
            p.stock +=1
            p.save()
        else:
            Cart.delete()
            p.stock +=1
            p.save()

    except:
        pass
    return cart_view(request)

def delete_cart(request,p):
    p = Product.objects.get(id=p)
    u = request.user
    try:
        Cart = cart.objects.get(user=u, product=p)
        Cart.delete()
        p.stock += cart.quantity
        p.save()

    except:
        pass
    return cart_view(request)

def orderform(request):
    if (request.method=="POST"):
        a=request.POST['a']
        p=request.POST['p']
        n=request.POST['n']



        u=request.user
        c=cart.objects.filter(user=u)

        total=0
        for i in c:
            total=total+i.quantity*i.product.price


        try:
            ac=Account.objects.get(acc_no=n)
            if(ac.amount >= total):

                ac.amount=ac.amount-total

                ac.save()
                for i in c:
                    o=Order.objects.create(user=u,product=i.product,address=a,phone=p,no_items=i.quantity,ordered_status="paid")
                    o.save()

                c.delete()
                msg="Order Placed Sucessfully"
                print(msg)
                return render(request,'orderdetail.html',{'message':msg})

            else:

                msg="Sorry,Insufficient balance"
                return render(request, 'orderdetail.html', {'message': msg})


        except:
            pass


    return render(request,'orderform.html')

@login_required
def orderview(request):

    u=request.user
    o = Order.objects.filter(user=u)

    return render(request,'orderview.html',{'o':o,'u':u.username})

