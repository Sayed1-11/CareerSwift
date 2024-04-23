from django.shortcuts import render,get_object_or_404,redirect,HttpResponseRedirect
from django.views.generic import DetailView,CreateView,ListView,View,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from jobs.models import Jobs
from job_seeker.models import Job_seeker
from category.models import Category
from contact_us.forms import Contactform
from jobs.forms import JobSearchForm
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your views here.


def send_transaction_email(email, subject, template):
        message = render_to_string(template, {
            
            
        })
        send_email = EmailMultiAlternatives(subject, '', to=[email])
  
        send_email.attach_alternative(message, "text/html")
        send_email.send()

# class HomeView(TemplateView):
#     template_name = 'index.html'

#     def get(self, request, industry=None):
#         data = Jobs.objects.all()
#         if industry is not None:
#             Industry = Category.objects.get(slug=industry)
#             data = Jobs.objects.filter(industry=Industry)
#         Industry = Category.objects.all()
        
#         if request.user.is_authenticated:
#             jobs, _ = Job_seeker.objects.get_or_create(user=request.user)
#         else:
#             jobs = None
#         return self.render_to_response({'data': data, 'industry': Industry,'jobs': jobs})
#     def post(self, request, *args, **kwargs):
#         form = JobSearchForm(request.POST)
#         if form.is_valid():
#             job_title = form.cleaned_data['job_title']
#             job_location = form.cleaned_data['job_location']
#             jobs = Jobs.objects.filter(title=job_title, location=job_location)
#             industries = Category.objects.all()  # Include industry data in context
#             context = {
#                 'data': jobs,
#                 'industry': industries,  # Pass industry data to the context
#                 'form': form,
#             }
#             return self.render_to_response(context)
#         else:
#             # If form is not valid, re-render the template with the form and error messages
#             data = Jobs.objects.all()
#             industries = Category.objects.all()
#             if request.user.is_authenticated:
#                 jobs, _ = Job_seeker.objects.get_or_create(user=request.user)
#             else:
#                 jobs = None
#             return self.render_to_response({'data': data, 'industry': industries, 'jobs': jobs, 'form': form})


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, industry=None):
        industries = Category.objects.all()
        data = Jobs.objects.all()
        job_title = request.GET.get('job-title', '')
        job_location = request.GET.get('job-location', '')

        if job_title:
            data = data.filter(title__icontains=job_title)
        if job_location:
            data = data.filter(location__name__icontains=job_location)

        if industry is not None:
            industry_instance = Category.objects.get(slug=industry)
            data = data.filter(industry=industry_instance)

        if request.user.is_authenticated:
            jobs, _ = Job_seeker.objects.get_or_create(user=request.user)
        else:
            jobs = None

        context = {
            'data': data,
            'industry': industries,
            'jobs': jobs,
            'search_query': {
                'job_title': job_title,
                'job_location': job_location,
            }
        }
        return self.render_to_response(context)

class Details(DetailView):
    model = Jobs
    pk_url_kwarg = 'id'
    template_name = "details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jobs = self.object            
        context['jobs']=jobs
        return context
    


    

def subsribe(request):
    if request.method == 'POST':
        email = request.POST.get('newsletter-email')
        send_transaction_email(email, "New Subsribtion", "subsribe_mail.html")
        return HttpResponseRedirect(reverse_lazy('home'))
    else:
        return HttpResponseRedirect(reverse_lazy('home'))
