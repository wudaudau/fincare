from django.urls import path
from . import views

urlpatterns = [
    # TODO: path('dashboard/', views.dashboard, name='dashboard'),
    # TODO: path('reports/', views.reports, name='reports'),
    path('transactions/', views.transactions, name='transactions'),
]