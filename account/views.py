from django.shortcuts import render,redirect
from django.views.generic import FormView,TemplateView
from . forms import RegistrationForm,ChangeUserForm
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here. 

class Registrationview(FormView):
    template_name = "register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy('profile')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
    
class Login(LoginView):
    template_name="login.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self) -> str:
        return reverse_lazy('home')
    

class Logout(LoginRequiredMixin,LogoutView):
    def get_success_url(self) -> str:
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    

    

class profile(LoginRequiredMixin,View):
    template_name = 'profile.html'

    def get(self, request):
        form = ChangeUserForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ChangeUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})
    


