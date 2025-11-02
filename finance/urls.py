from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),  # welcome page with login form
    path('menu/', views.menu, name='menu'),  # Menu page for authenticated users
    # TODO: path('dashboard/', views.dashboard, name='dashboard'),
    # TODO: path('reports/', views.reports, name='reports'),
    path('transaction_list/', views.transaction_list, name='transaction_list'),
    path('logout/', auth_views.LogoutView.as_view(next_page='welcome'), name='logout'),  # Logout redirects to welcome
]