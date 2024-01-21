from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='employees')
    company_name = models.CharField(max_length=70)

    def __str__(self) -> str:
        return self.company_name