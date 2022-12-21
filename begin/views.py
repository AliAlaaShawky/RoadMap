from django.shortcuts import render
from .models import StartCourse,StartTrack,CourseCV,trackCV
from home.models import Courses,Track,CoursesContent,TrackContent
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime

# Create your views here.
def begin(request,start_id,start_name):
    if request.user.is_authenticated and StartCourse.objects.filter(startcourse=start_id).exists():
        start=StartCourse.objects.get(startcourse=start_id)
        return render(request,'start/about.html',{'start':start})
   
    return render(request,'start/about.html')
def trackbegin(request,begin_id,begin_name):
    if request.user.is_authenticated and StartTrack.objects.filter(starttrack=begin_id).exists():
        trackstart=StartTrack.objects.get(starttrack=begin_id)
        return render(request,'start/begin.html',{'trackstart':trackstart})
   
    return render(request,'start/begin.html')
def mycv(request):
    if request.user.is_authenticated :
        trac,core=None,None
        user_id=request.user.id
        if CourseCV.objects.filter(user=user_id).exists():
            courses=[]
            list=[]
            content=CourseCV.objects.all().filter(user=user_id)
            for names in content:
                courses.append(names.finishedCourse.all())
            for i in courses:
                for items in i:
                    list.append(items)
            core=CoursesContent.objects.all().filter(CName__in=list)
        if trackCV.objects.filter(user=user_id).exists():
                tracks=[]
                lists=[]
                contents=trackCV.objects.all().filter(user=user_id)
                for name in contents:
                    tracks.append(name.finishedTrack.all())
                for x in tracks:
                    for item in x:
                        lists.append(item)
                trac=TrackContent.objects.all().filter(TName__in=lists)
        return render(request,'start/cart.html',{'core':core,'trac':trac})

    return render(request,'start/cart.html',{})
