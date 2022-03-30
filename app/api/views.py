from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework.views import APIView
import django.contrib.messages as messages
from django.db import reset_queries
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import LoanDetailSerializer
from django.contrib.auth.models import User
from api.models import LOAN_CALCULATION
import jwt, datetime, logging

class CalcView(APIView):
    def get(self,request):
        logging.warning(request.data)
        data = request.data
        serializer = LoanDetailSerializer(data)

        result = {}

        r = 0.24
        n = data["loan_term"]
        p =  data["loan_amount"]
        mpa = p * (r*(1 + r) **n) / ((1 + r) **n - 1)
        tia = (mpa*n) - p

        result["principal_loan_amt"] = p
        result["monthly_payment_amt"] = round(mpa, 2)
        result["total_interest_amount"] = round((mpa*n) - p, 2)
        result["total_sum_of_payments"] = round(p + tia, 2)


        
        return Response(result)

    def post(self,request):
        logging.warning(request.data)
        data = request.data
        result = {}

        r = 0.24
        n = data["loan_term"]
        p =  data["loan_amount"]
        mpa = p * (r*(1 + r) **n) / ((1 + r) **n - 1)
        tia = (mpa*n) - p

        #['id', 'first_name', 'middle_name', 'last_name', 'loan_amount', 'loan_term', 'total_interest', 'monthly_payment', 'total_sum']
        result["first_name"] = data["first_name"]
        result["middle_name"] = data["middle_name"]
        result["last_name"] = data["last_name"]
        result["loan_amount"] = data["loan_amount"]
        result["loan_term"] = n
        result["total_interest"] = round((mpa*n) - p, 2)
        result["monthly_payment"] = round(mpa, 2)
        result["total_sum"] = round(p + tia, 2)

        serializer = LoanDetailSerializer(data=result)

        logging.warn(serializer)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        
        return Response(serializer.data)
        