from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from .models import Transaction

# Create your views here.
def welcome(request):
    form = AuthenticationForm()
    return render(request, 'finance/welcome.html', {'form': form})


def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-date')
    return render(request, 'finance/transaction_list.html', {'transactions': transactions}) 