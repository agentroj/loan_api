from .views import CalcView
from django.urls import path

urlpatterns = [
    path('loan_calculator/', CalcView.as_view()),
]