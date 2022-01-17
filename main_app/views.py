from django.http import HttpResponse
from django.shortcuts import render

# import HttpResponse to test view functions
# will delete after imlementing templates
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>test</h1>')