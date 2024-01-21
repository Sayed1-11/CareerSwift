from .models import Jobs,JobApplication
from employee.models import Employee
from django import forms


class JobsForm(forms.ModelForm):
    class Meta:
        model = Jobs
        exclude= ['posted_by']
    def __init__(self,*args, **kwargs):
        super(JobsForm, self).__init__(*args, **kwargs)


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['letter']
        
    def __init__(self,*args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)

class JobSearch(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['title','location']
        
    def __init__(self,*args, **kwargs):
        super(JobSearch, self).__init__(*args, **kwargs)

   