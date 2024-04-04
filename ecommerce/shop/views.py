from django.shortcuts import render,redirect
from shop.models import Category,Product
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.

# for displaying all categories
def allcategories(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})

# for displaying product under a particular categories

def allproducts(request,pk):
    c=Category.objects.get(id=pk)
    p=Product.objects.filter(category=c)
    return render(request,'products.html',{'c':c,'p':p})

def showdetail(request,p):
    pro=Product.objects.get(id=p)
    return render(request,'detail.html',{'pro':pro})

def register(request):
    if(request.method=="POST"):
        u = request.POST['u']
        e = request.POST['e']
        p = request.POST['p']
        cp = request.POST['cp']
        f = request.POST['f']
        l = request.POST['l']

        if(cp==p):
            user=User.objects.create_user(username=u,email=e,password=p,first_name=f,last_name=l)
            user.save()
            return allcategories(request)
        else:
            return HttpResponse("Password are not same")
    return render(request,'register.html')

def U_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)

        if user:
            login(request,user)
            return allcategories(request)
        else:
            return HttpResponse("invalid Credentials")

    return render(request,'login.html')


def U_logout(request):
    logout(request)
    return allcategories(request)



