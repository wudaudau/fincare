from django.test import TestCase


######
# Test Models
######

from django.contrib.auth.models import User
from .models import UserProfile, Transaction, Category

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(name='Healthcare')

    def test_user_profile_creation(self):
        profile = UserProfile.objects.create(user=self.user, bio='Test bio')
        self.assertEqual(profile.user.username, 'testuser')
        self.assertEqual(profile.bio, 'Test bio')

    def test_transaction_creation(self):
        transaction = Transaction.objects.create(
            user=self.user,
            type='income',
            category=self.category.name,
            amount=100.50,
            description='Test income',
            date='2023-10-01'
        )
        self.assertEqual(transaction.user.username, 'testuser')
        self.assertEqual(transaction.type, 'income')
        self.assertEqual(transaction.amount, 100.50)
        self.assertEqual(str(transaction), 'Income of 100.5 on 2023-10-01 by testuser')

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Healthcare')
        self.assertEqual(str(self.category), 'Healthcare')


######
# Test Views
######

from django.urls import reverse

class ViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

    def test_transaction_list_view(self):
        url = reverse('transaction_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance/transaction_list.html')


######
# Test URLs
######

from django.urls import resolve

class URLTests(TestCase):
    def test_transaction_list_url_resolves(self):
        url = reverse('transaction_list')
        resolver = resolve(url)
        self.assertEqual(resolver.view_name, 'transaction_list')


######
# Test Forms
######