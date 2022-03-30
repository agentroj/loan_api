from django.db import models

# Create your models here.
class LOAN_CALCULATION(models.Model):
    first_name = models.CharField(null = True, max_length=256)
    middle_name = models.CharField(null = True, max_length=256)
    last_name = models.CharField(null = True, max_length=256)
    loan_amount = models.IntegerField(default=0)
    loan_term = models.IntegerField(default=0)
    total_interest = models.FloatField(default=0)
    monthly_payment = models.FloatField(default=0)
    total_sum = models.FloatField(default=0)