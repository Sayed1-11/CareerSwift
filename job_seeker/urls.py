
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('job_seeker/',views.Job_seeker.as_view(),name='seeker'),

    
]
