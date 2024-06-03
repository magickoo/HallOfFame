from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login,logout , authenticate
from .models import Hall
# Create your views here.
def home(request):
    return render(request,'halls/home.html')



def logoutuser(request):
    logout(request)
    return redirect('home')  # Redirect to home if the request method is not POST


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'
    
    def form_valid(self, form):
        view = super(SignUp,self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view
    
#def create_view(request):
    #if request.method == 'POST':
        # get the form data
        # validate the form data
        # create hall
        # save hall
    #else:
        # Create a form for hall
        # return the hall
        
        
class CreateHall(generic.CreateView):
    model = Hall
    fields = ['title']
    template_name = 'halls/create_hall.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        super(CreateHall,self).form_valid(form)
        return redirect('home')
    
