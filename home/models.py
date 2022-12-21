from django.db import models
# Create your models here.

class CoursesContent(models.Model):
    CName=models.CharField(verbose_name='Course Name',max_length=40,null=False)
    cImg=models.ImageField(verbose_name='Course Image',upload_to='photo')
    cDescription=models.TextField(verbose_name='Course Description',max_length=200,null=False)
    class Meta:
        ordering=['id']
    def __str__(self) :
        return self.CName
class TrackContent(models.Model):
    TName=models.CharField( verbose_name='Track Name',max_length=40,null=False)
    Tmg=models.ImageField(verbose_name='Track Image',upload_to='photo')
    TDescription=models.TextField(verbose_name='Track Description',max_length=200,null=False)
    class Meta:
        ordering=['id']
    def __str__(self) :
        return self.TName
class Courses(models.Model):
    courseContent=models.ManyToManyField(CoursesContent)
    CourseName=models.CharField(max_length=40,null=False)
    courseImg=models.ImageField(upload_to='photo')
    courseDescription=models.TextField(max_length=200,null=False)
    class Meta:
        ordering=['-id']
    def __str__(self) :
        return self.CourseName
class Track(models.Model):
    TrackContent=models.ManyToManyField(TrackContent)
    TrackName=models.CharField(max_length=40,null=False)
    TrackImg=models.ImageField(upload_to='photo')
    TrackDescription=models.TextField(max_length=200,null=False)
    class Meta:
        ordering=['-id']
    def __str__(self) :
        return self.TrackName