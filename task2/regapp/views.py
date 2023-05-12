from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


# Create your views here.

def login(request):
    if request.method=='POST':
        name=request.POST['username']
        lock=request.POST['password']
        user=auth.authenticate(username=name,password=lock)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid user name or password ')
            return redirect('login')

    return render(request,'login.html')


def register(request):
    if request.method == "POST":
        user=request.POST['user name']
        first=request.POST['first name']
        last=request.POST['last name']
        mail=request.POST['email']
        lock1=request.POST['password1']
        lock2=request.POST['password2']
        if lock1==lock2:
            if User.objects.filter(username=user).exists():
                messages.info(request,'user name already exists')
                return redirect('register')
            elif User.objects.filter(email=mail).exists():
                messages.info(request,' email already exists')
                return redirect('register')
            else:
                member = User.objects.create_user(username=user, first_name=first, last_name=last, email=mail, password=lock1)
                member.save();
                print("user created")
                return redirect('login')
        else:
            messages.info(request, 'not matching')
            return redirect('register')

        return redirect('/')
    return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')