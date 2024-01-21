from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import CreateView,ListView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import Seekerform

class Job_seeker(LoginRequiredMixin, CreateView):
    template_name = 'job_seeker.html'
    form_class  = Seekerform
    success_url = reverse_lazy('home')

    def form_valid(self, form) :
        form.instance.user = self.request.user
        return super().form_valid(form)