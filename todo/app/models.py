from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,)
    label = models.CharField(max_length=200)
    description =models.TextField()
    create_date = models.DateTimeField(default=datetime.now())

    def get_absolute_url(self):
        return reverse('app:detail',args=[self.id])

    def __str__(self):
        return self.label

class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(blank=True,default='default.jpg',upload_to='profile_pic')

    def __str__(self):
        return '{} profile'.format(self.user.username)