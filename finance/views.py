from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Transaction

# Create your views here.
def welcome(request):
    form = AuthenticationForm()
    return render(request, 'finance/welcome.html', {'form': form})

@login_required
def menu(request):
    return render(request, 'finance/menu.html')

def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-date')
    return render(request, 'finance/transaction_list.html', {'transactions': transactions}) 