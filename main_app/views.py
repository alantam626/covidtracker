import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Strategy, Kit, State
from .forms import KitForm, StrategyForm, UserForm

# Create your views here.
def home(request):
    states = State.objects.all()
    google_api_key = os.environ['GOOGLE_API_KEY']
    return render(request, 'home.html', { 'states': states, 'google_api_key': google_api_key })

@login_required
def kits_index(request):
    return render(request, 'covidtracker/index.html')

@login_required
def strategies_index(request):
    strategies = Strategy.objects.all()
    return render(request, 'main_app/strategies_index.html', { 'strategies': strategies })

@login_required
def strategies_detail(request, strategy_id):
    strategy = Strategy.objects.get(id=strategy_id)
    return render(request,'main_app/strategies_detail.html', {'strategy': strategy})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            login(request, user)
            return redirect('kits_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserForm()
    context = {'form': form, 'error_message': error_message}
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

@login_required
def create_strategy(request):
    form = StrategyForm(request.POST)
    if form.is_valid():
        new_strategy = form.save(commit=False)
        new_strategy.save()
    return redirect('detail')

    
@login_required
def kits_detail(request, kit_id):
    if request.user.kit_set.filter(id=kit_id).exists():
        kits = Kit.objects.get(id=kit_id)
        return render(request, 'kits/detail.html')

@login_required
def create_kit(request, user_id):
    form = KitForm(request.POST)
    if form.is_valid():
        new_kit = form.save(commit=False)
        new_kit.user_id = user_id
        new_kit.save()
    return redirect('kits_detail', user_id=user_id)

class KitCreate (LoginRequiredMixin, CreateView):
    model = Kit
    fields = '__all__'
    def form_valid(self, form):
  
      form.instance.user = self.request.user 
      return super().form_valid(form)

class KitDetail(LoginRequiredMixin, DetailView):
    model = Kit

class KitUpdate(LoginRequiredMixin, UpdateView):
    model = Kit
    fields = '__all__'

class KitDelete(LoginRequiredMixin, DetailView):
    model = Kit
    success_url = '/kits_index/'