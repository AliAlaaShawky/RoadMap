from django.db import models
from django.contrib.auth.models import User
from home.models import Courses,Track
# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Courses,on_delete=models.CASCADE,null=True)
    track=models.ForeignKey(Track,on_delete=models.CASCADE,null=True)
    Address=models.CharField(max_length=200,null=False)
    def __str__(self):
        return self.user.username
