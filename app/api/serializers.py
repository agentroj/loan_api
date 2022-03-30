from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import LOAN_CALCULATION

class LoanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LOAN_CALCULATION
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'loan_amount', 'loan_term', 'total_interest', 'monthly_payment', 'total_sum']
        extra_kwargs = {
            'model': {'write_only': True}
        }
    def create(self, validated_data):
        loan_dtl_id = validated_data.pop('id', None)
        instance = self.Meta.model(**validated_data)
        if loan_dtl_id is not None:
            instance.set_password(loan_dtl_id)
        instance.save() 
        return instance