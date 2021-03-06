# Generated by Django 3.2.3 on 2022-03-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan_calculation',
            name='monthly_payment',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='loan_calculation',
            name='total_interest',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='loan_calculation',
            name='total_sum',
            field=models.FloatField(default=0),
        ),
    ]
