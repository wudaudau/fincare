from django.shortcuts import render
from .models import Transaction

# Create your views here.
def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-date')
    return render(request, 'finance/transaction_list.html', {'transactions': transactions}) 