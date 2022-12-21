from django.contrib import admin
from .models import StartCourse,StartTrack,CourseCV,trackCV
# Register your models here.
admin.site.register(StartCourse)
admin.site.register(StartTrack)
admin.site.register(CourseCV)
admin.site.register(trackCV)
