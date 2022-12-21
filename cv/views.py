from unittest import result
from django.shortcuts import redirect, render
from matplotlib.style import context
from begin.models import StartCourse,StartTrack,CourseCV,trackCV
from home.models import Courses,Track,CoursesContent,TrackContent
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime
# Create your views here.
def cv(request,start,course_name):
    if request.user.is_authenticated:
        
        if not  CourseCV.objects.filter(user=request.user.id,finishedCourse=start).exists():
                user=User.objects.get(id=request.user.id)
                course=CoursesContent.objects.get(id=start)
                time=str(datetime.now())
                obj=CourseCV()
                obj.user=user
                try:
                    obj.finishedCourse.add(course)
                except:
                    obj.finishedDate=time
                    obj.save()
                    obj.finishedCourse.add(course)
                    obj.save()
                coursedetails =CoursesContent.objects.get(id=start)
                messages.success(request,'Added Successfully')
                context={
                'coursedetails':coursedetails
                }
                return render(request,'home/course.html',context)
        coursedetails=CoursesContent.objects.get(id=start)
        context={
            'coursedetails':coursedetails
            }
        messages.error(request,'already added')
        return render(request,'home/course.html' , context)
    messages.error(request,'failed to add')
    return render(request,'home/course.html',{})
def trackcv(request,start,course_name):
    if request.user.is_authenticated:
        
        if not  trackCV.objects.filter(user=request.user.id,finishedTrack=start).exists():
                user=User.objects.get(id=request.user.id)
                course=TrackContent.objects.get(id=start)
                time=str(datetime.now())
                obj=trackCV()
                obj.user=user
                try:
                    obj.finishedTrack.add(course)
                except:
                    obj.finishedDate=time
                    obj.save()
                    obj.finishedTrack.add(course)
                    obj.save()
                trackdetails =TrackContent.objects.get(id=start)
                messages.success(request,'Added Successfully')
                context={
                'trackdetails':trackdetails
                }
                return render(request,'home/track.html',context)
        trackdetails=TrackContent.objects.get(id=start)
        context={
            'trackdetails':trackdetails
            }
        messages.error(request,'already added')
        return render(request,'home/track.html' , context)
    messages.error(request,'failed to add')
    return render(request,'home/track.html',{})
