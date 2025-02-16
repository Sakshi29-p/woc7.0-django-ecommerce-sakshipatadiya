from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

from .models import Product,Category,Profile

from django.db.models import Q

import json

from cart.cart import Cart

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})

def login_user(request):
    if request.method =="POST":
        password = request.POST.get('password')
        email = request.POST.get('email')

        if not User.objects.filter(email=email).exists():
            messages.error(request,'Account Not registered')
            return redirect('/login/')
        else:
            usern = User.objects.get(email=email)
        
        user = authenticate(username=usern.username,password=password)
        
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('login_user')
        else:
            login(request,user)

            # shopping cart
            current_user = Profile.objects.get(user__id=request.user.id)
            saved_cart = current_user.old_cart
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                cart = Cart(request)

                for key,value in converted_cart.items():
                    cart.db_add(product=key,quantity=value)


            messages.success(request,("You have been logged in...."))
            return redirect('index')
        

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,("You have been logged out...."))
    return redirect('/')

def register_user(request):
    if request.method =="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'Username already exists.')
            return redirect('register_user')
        
        mail = User.objects.filter(email=email)
        if mail.exists():
            messages.info(request,'Email already registered.')
            return redirect('register_user')
        

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email
        )

        user.set_password(password)
        user.save()
        login(request,user)
        messages.info(request,'Account created successfully......')

        return redirect('index')

    return render(request, 'register.html')


def about(request):
    return  render(request, 'about.html')

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product})

def category(request,foo):
    foo = foo.replace('-',' ')

    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request,'category.html',{'products':products,'category':category})
    except:
        messages.success(request,("That category doesnt exists....."))
        return redirect('index')
    
def allCategory(request):
    categories = Category.objects.all()
    return render(request,'allCategory.html',{'categories':categories})


def update_user(request):
    return render(request,'update_user.html',{})


def search(request):
    if request.method=="POST":
        searched = request.POST['searched'] 

        # Query the Products
        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))

        if not searched:
            messages.success(request,("This type of product doesnt exists..."))
            return render(request,"search.html",{})
        else:
            return render(request,"search.html",{'searched':searched})
    else:
        return render(request,"search.html",{})