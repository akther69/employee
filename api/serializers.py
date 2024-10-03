from rest_framework import serializers

from Myapp.models import Employee,Work

from rest_framework.response import Response

class WorkSerializer(serializers.ModelSerializer):
    
    employee_object=serializers.StringRelatedField()
    
    class Meta:
        
        model=Work
        
        fields="__all__"
        
        read_only_fields=["id","employee_object"]

class EmployeeSerializer(serializers.ModelSerializer):
    
    # works=WorkSerializer(read_only=True,many=True)
    
    works=serializers.SerializerMethodField(read_only=True)
    
    # work_count=serializers.IntegerField(read_only=True)
    
    work_count=serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        
        model=Employee
        
        # fields="__all__"
        
        fields=["id","name","age","designation","salary","email","phone","place","work_count","works"]
        
        # always give get as prefix when writing custom method
        
        
    def get_work_count(self,obj):
        
        return Work.objects.filter(employee_object=obj).count()
    
    def get_works(self,obj):
        
        qs=Work.objects.filter(employee_object=obj)
        
        serializer_instance=WorkSerializer(qs,many=True)
        
        return serializer_instance.data