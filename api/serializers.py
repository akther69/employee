from rest_framework import serializers

from Myapp.models import Employee,Work

class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model=Employee
        
        fields="__all__"