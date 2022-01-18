from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kits_index/', views.kits_index, name='kits_index'),
    path('accounts/signup/', views.signup, name='signup'),
<<<<<<< HEAD
    path('strategies/', views.strategies_index, name='strategies_index'),
    path('strategies/<int:strategy_id>', views.strategies_detail, name='strategies_detail'),
    path('strategies/create/', views.StrategyCreate.as_view(), name='strategies_create'),
    path('strategies/<int:strategy_id>/update', views.StrategyUpdate.as_view(), name='strategies_update'),
    path('strategies/<int:strategy_id>/delete', views.StrategyDelete.as_view(), name='strategies_delete'),
=======
    path('kits/create/', views.KitCreate.as_view(), name ='kits_create'),
>>>>>>> f613ec751404ce00871fc246c00637b8ff999297
]