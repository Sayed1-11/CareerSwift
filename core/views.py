from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import DetailView,CreateView,ListView,View,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from jobs.models import Jobs
from category.models import Category
from contact_us.forms import Contactform
from jobs.forms import JobSearch
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your views here.

class HomeView(TemplateView):
    template_name = 'base.html'
    form_class = JobSearch

    def get(self, request,industry=None):
        data = Jobs.objects.all()
        if industry is not None:
            Industry = Category.objects.get(slug=industry)
            data = Jobs.objects.filter(industry=Industry)
        Industry = Category.objects.all()
        return self.render_to_response({'data': data, 'industry': Industry})
    

class Details(DetailView):
    model = Jobs
    pk_url_kwarg = 'id'
    template_name = "details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jobs = self.object            
        context['jobs']=jobs
        return context
    

class Contact_us(FormView):
    template_name = "contact.html"
    form_class = Contactform
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    