from django.contrib import admin

# Register your models here.
from .models import Courses,Track,TrackContent,CoursesContent
# Register your models here.
admin.site.register(Courses)
admin.site.register(Track)
admin.site.register(TrackContent)
admin.site.register(CoursesContent)
