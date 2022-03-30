import imp
from django.contrib import admin

# Register your models here.
from .models import LOAN_CALCULATION

admin.site.register(LOAN_CALCULATION)