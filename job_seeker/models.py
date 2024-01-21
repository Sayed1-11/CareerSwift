from django.db import models
from django.contrib.auth.models import User
from location.models import Location

# Create your models here.
class Job_seeker(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='seeker')
    bio = models.TextField()
    resume = models.TextField(default=None)
    

    def __str__(self) -> str:
        return self.user.username