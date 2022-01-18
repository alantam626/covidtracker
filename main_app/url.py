from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kits_index/', views.kits_index, name='kits_index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('kits/create/', views.KitCreate.as_view(), name ='kits_create'),
]