from django.contrib import admin
from .models import UserProfile, Transaction, Category

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Transaction)
admin.site.register(Category)