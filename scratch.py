#views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Strategy, Kit


# import HttpResponse to test view functions

# will delete after imlementing templates
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def kits_index(request):
    return render(request, 'covidtracker/index.html')

def strategies_index(request):
    strategies = Strategy.objects.all()
    return render(request, 'main_app/strategies_index.html', { 'strategies': strategies })

def strategies_detail(request, strategy_id):
    strategy = Strategy.objects.get(id=strategy_id)
    return render(request,'main_app/strategies_detail.html', {'strategy': strategy})

def signup(request):
    error_mesage = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error-message': error_mesage}
    return render(request, 'registration/signup.html', context)

class StrategyCreate(CreateView):
    model = Strategy
    fields = '__all__'

class StrategyUpdate(UpdateView):
    model = Strategy
    fields = ['rating', 'type']

    
class StrategyDelete(DeleteView):
    model = Strategy
    success_url = '/strategies_index/'

#urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kits_index/', views.kits_index, name='kits_index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('strategies/', views.strategies_index, name='strategies_index'),
    path('strategies/<int:strategy_id>', views.strategies_detail, name='strategies_detail'),
    path('strategies/create/', views.StrategyCreate.as_view(), name='strategies_create'),
    path('strategies/<int:strategy_id>/update', views.StrategyUpdate.as_view(), name='strategies_update'),
    path('strategies/<int:strategy_id>/delete', views.StrategyDelete.as_view(), name='strategies_delete'),
]

