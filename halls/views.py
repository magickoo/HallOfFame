from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import Hall
# Create your views here.
def home(request):
    return render(request,'halls/home.html')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'
    
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