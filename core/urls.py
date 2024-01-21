from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('industry/<slug:industry>',views.HomeView.as_view(),name='industry'),
    path('details/<int:id>',views.Details.as_view(),name='details'),
    path('contact/',views.Contact_us.as_view(),name='contact')
    
]
