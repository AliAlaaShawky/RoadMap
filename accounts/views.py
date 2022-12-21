from django.shortcuts import redirect, render
from matplotlib.style import use
from .models import UserProfile
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib import auth
from django.contrib.auth.models import User
from begin.models import StartCourse,StartTrack,CourseCV,trackCV
from home.models import Courses,Track,CoursesContent,TrackContent
from datetime import datetime

# Create your views here.
def login(request):
    if request.method=='POST'and 'submit' in request.POST:
        password,username=None,None
        if 'username'in request.POST:username=request.POST['username']
        else:messages.error(request,'enter user name')
        if'password' in request.POST:password=request.POST['password']
        else:messages.error(request,'enter password')
        user=auth.authenticate(password=password,username=username)
        if user is not None:
            if 'remember' in request.POST:
                request.session.set_expiry(0)
            auth.login(request,user)
            messages.success(request,"login successfully")
            return redirect('home')
        else:messages.error(request,'user name or password in incorrect')  
        context={'username':username}
        return render(request,'accounts/login.html',context)
    return render(request,'accounts/login.html',{})
def signup(request):
    if request.method=='POST' and 'submit' in request.POST:
        terms,fname,lname,uname,email,password,address=None,None,None,None,None,None,None
        if 'fname' in request.POST:fname= request.POST['fname']
        else:messages.error(request,'please enter first name')
        if'lname' in request.POST: lname=request.POST['lname']
        else:messages.error(request,'please enter last name')
        if 'uname' in request.POST:uname=request.POST['uname']
        else:messages.error(request,'please enter user name')
        if 'password' in request.POST:password=request.POST['password']
        else:messages.error(request,'please enter user name')
        if 'email' in request.POST:email=request.POST['email']
        else:messages.error(request,'please enter email')
        if 'address' in request.POST:address=request.POST['address']
        else:messages.error(request,'please enter address')
        if 'accept' in request.POST:terms=request.POST['accept']
        if terms=='on':
            if not User.objects.filter(username=uname).exists():
                try:
                    validate_email(email)
                    if not User.objects.filter(email=email).exists():
                        user=User.objects.create(first_name=fname,
                        last_name=lname,username=uname,
                        password=password,email=email
                        )
                        userprofile=UserProfile.objects.create(user=user,Address=address)
                        user.save()
                        userprofile.save()
                        #clear value
                        fname,lname,uname,email,password,address='','','','','',''
                        messages.success(request,'account created successfully')
                    else:messages.error(request,'user E-mail already exist')  
                except ValidationError:messages.error(request,'Enter valid E-mail please')
            else:messages.error(request,'user name already exist')  
        else:messages.error(request,'you should accept terms')
        context={
            'fname':fname,
            'lname':lname,
            'uname':uname,
            'password':password,
            'email':email,
            'address':address 
            }
        return render(request,'accounts/signup.html',context)
    return render(request,'accounts/signup.html',{})
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('home')
def profile(request):
    if request.user.is_authenticated:
        firstname=None
        lastname=None
        email=None
        username=None
        address=None
        if request.method=='POST' and 'update' in request.POST:
            if 'firstname' in request.POST: firstname=request.POST['firstname']
            else:messages.error(request,'enter new first name')
            if 'lastname' in request.POST: lastname=request.POST['lastname']
            else:messages.error(request,'enter new first name')
            if 'address' in request.POST: address=request.POST['address']
            else:messages.error(request,'enter new first name')
            if 'password' in request.POST: password=request.POST['password']
            else:messages.error(request,'enter new first name')
            if 'username' in request.POST: username=request.POST['username']
            else:messages.error(request,'enter new first name')
            if 'email' in request.POST: email=request.POST['email']
            else:messages.error(request,'enter new first name')
            newdata=User.objects.get(id=request.user.id)
            newdata2=UserProfile.objects.get(user=request.user.id)
            newdata.first_name=firstname
            newdata.last_name=lastname
            newdata2.Address=address
            print(password)
            print(username)
            newdata.set_password(password)  
            newdata.save()
            newdata2.save()
            user=auth.authenticate(password=password,username=username)
            if user is not None:
                auth.login(request,user)
                context={
                'firstname':firstname,
                'lastname':lastname,
                'email':email,
                'username':username,
                'address':address,}
                messages.success(request,"update your data successfully")
                return render(request,'accounts/profile.html',context)
        data=User.objects.get(id=request.user.id)
        data2=UserProfile.objects.get(user=request.user.id)
        firstname=data.first_name
        lastname=data.last_name
        email=data.email
        username=data.username
        address=data2.Address
        context={
            'firstname':firstname,
            'lastname':lastname,
            'email':email,
            'username':username,
            'address':address,
        }
        return render(request,'accounts/profile.html',context)
    return render(request,'accounts/profile.html',{})