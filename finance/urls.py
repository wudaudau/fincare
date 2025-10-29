from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),  # welcome page
    # TODO: path('dashboard/', views.dashboard, name='dashboard'),
    # TODO: path('reports/', views.reports, name='reports'),
    path('transaction_list/', views.transaction_list, name='transaction_list'),
]