from rest_framework import serializers
from .models import bankDetails





class bankSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = bankDetails
        fields = ['ifsc', 'bank_id',
                  'branch', 'address', 'city', 'district', 'state','bank_name']
    


                  





