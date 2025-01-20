from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    if request.method =="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'Username already exists.')
            return redirect('/register/')
        
        mail = User.objects.filter(email=email)
        if mail.exists():
            messages.info(request,'Email already registered.')
            return redirect('/register/')
        

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email
        )

        user.set_password(password)
        user.save()
        messages.info(request,'Account created successfully.')

        return redirect('/register/')

    return render(request, 'register.html')