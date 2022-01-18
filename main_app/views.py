from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Kit
from .forms import KitForm

# import HttpResponse to test view functions
# will delete after imlementing templates
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def kits_index(request):
    return render(request, 'covidtracker/index.html')


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

@login_required
def kits_detail(request, kit_id):
    if request.user.kit_set.filter(id=kit_id).exists():
        kit = Kit.objects.get(id=kit_id)

# @login_required
# def create_kit(request, user_id):
#     form = KitForm(request.POST)
#     if form.is_valid():
#         new_kit = form.save(commit=False)
#         new_kit.user_id = user_id
#         new_kit.save()
#     return redirect('detail', user_id=user_id)


class KitCreate (LoginRequiredMixin, CreateView):
    model = Kit
    fields = '__all__'