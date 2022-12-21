from django.db import models
from home.models import CoursesContent,TrackContent
from django.contrib.auth.models import User
# Create your models here.
class StartCourse(models.Model):
    startcourse=models.ForeignKey(CoursesContent,on_delete=models.CASCADE)
    courseAdvice=models.TextField()
    youtubeSource1=models.CharField(max_length=200)
    imgSource1=models.ImageField(upload_to='photo')
    desSource1=models.CharField(max_length=200)
    youtubeSource2=models.CharField(max_length=200)
    imgSource2=models.ImageField(upload_to='photo')
    desSource2=models.CharField(max_length=200)
    documentSource1=models.CharField(max_length=200)
    imgSource3=models.ImageField(upload_to='photo')
    desSource3=models.CharField(max_length=200)
    documentSource2=models.CharField(max_length=200)
    imgSource4=models.ImageField(upload_to='photo')
    desSource4=models.CharField(max_length=200)

    def __str__(self):
        return self.startcourse.CName
class StartTrack (models.Model):
    starttrack=models.ForeignKey(TrackContent,on_delete=models.CASCADE)
    trackAdvice=models.TextField()
    youtubeSource1=models.CharField(max_length=200)
    imgSource1=models.ImageField(upload_to='photo')
    desSource1=models.CharField(max_length=200)
    youtubeSource2=models.CharField(max_length=200)
    imgSource2=models.ImageField(upload_to='photo')
    desSource2=models.CharField(max_length=200)
    documentSource1=models.CharField(max_length=200)
    imgSource3=models.ImageField(upload_to='photo')
    desSource3=models.CharField(max_length=200)
    documentSource2=models.CharField(max_length=200)
    imgSource4=models.ImageField(upload_to='photo')
    desSource4=models.CharField(max_length=200)

    def __str__(self):
        return self.starttrack.TName
class CourseCV(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    finishedCourse=models.ManyToManyField(CoursesContent)
    finishedDate=models.DateTimeField()
    class Meta:
        ordering=['-finishedDate']
    def __str__(self):
        return self.user.username
class trackCV(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    finishedTrack=models.ManyToManyField(TrackContent)
    finishedDate=models.DateTimeField()
    class Meta:
        ordering=['-finishedDate']
    def __str__(self):
        return self.user.username