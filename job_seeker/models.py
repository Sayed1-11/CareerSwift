from django.db import models
from django.contrib.auth.models import User
from location.models import Location

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Job_seeker(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='seeker')
    CareerObjective = models.TextField(null=True)
    skills = models.ManyToManyField(Skill)
    projects_name = models.TextField(null=True, blank=True)
    Experience = models.TextField(null=True, blank=True)
    about_me = models.TextField(null=True)
    Contact = models.CharField(max_length=12,null=True)
    github_link = models.CharField(max_length=500,null=True)
    others_link = models.CharField(max_length=256,null=True,blank=True)

   

    def __str__(self) -> str:
        return self.user.username
