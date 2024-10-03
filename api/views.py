from django.shortcuts import render

from rest_framework.views import APIView

from Myapp.models import Employee

from api.serializers import EmployeeSerializer

from rest_framework.response import Response

from rest_framework import viewsets

from rest_framework.decorators import action

from rest_framework import generics

# Create your views here.

class EmployeeCreateListView(APIView):
    
    def get(self,request,*args, **kwargs):
        
        qs=Employee.objects.all()
        
        serializer_instance=EmployeeSerializer(qs,many=True)
        
        return Response(data=serializer_instance.data)
    
    
    def post(self,request,*args, **kwargs):
        
        serializer_instance=EmployeeSerializer(data=request.data)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save()
            
            return Response(data=serializer_instance.data)
        
        return Response(data=serializer_instance.errors)
    
class EmployeeRetrieveUpdateDestroyView(APIView):
    
    def get(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        qs=Employee.objects.get(id=id)
        
        serializer_instance=EmployeeSerializer(qs)
        
        return Response(data=serializer_instance.data)
    
    def put(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        employee_obj=Employee.objects.get(id=id)
        
        serializer_instance=EmployeeSerializer(data=request.data,instance=employee_obj)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save()
            
            return Response(data=serializer_instance.data)
        
        return Response(data=serializer_instance.errors)
    
    
    def delete(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        Employee.objects.get(id=id).delete()
        
        data={"message":"deleted"}
        
        return Response(data)
    
class EmployeeViewsetView(viewsets.ViewSet):
    
    def list(self,request,*args, **kwargs):
        
        qs=Employee.objects.all()
        
        serializer_instance=EmployeeSerializer(qs,many=True)
        
        return Response(data=serializer_instance.data)
    
    
    def create(self,request,*args, **kwargs):
        
        serializer_instance=EmployeeSerializer(data=request.data)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save()
            
            return Response(data=serializer_instance.data)
        
        return Response(data=serializer_instance.errors)
    
    def retrieve(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        qs=Employee.objects.get(id=id)
        
        serializer_instance=EmployeeSerializer(qs)
        
        return Response(data=serializer_instance.data)
    
    def update(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        employee_obj=Employee.objects.get(id=id)
        
        serializer_instance=EmployeeSerializer(data=request.data,instance=employee_obj)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save()
            
            return Response(data=serializer_instance.data)
        
        return Response(data=serializer_instance.errors)
    
    
    def destroy(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        Employee.objects.get(id=id).delete()
        
        data={"message":"deleted"}
        
        return Response(data)
    
    
    @action(methods=["GET"],detail=False)
    
    def designation_list(self,request,*args, **kwargs):
        
        designation=Employee.objects.all().values_list("designation",flat=True).distinct()
        
        return Response(data=designation)
    
class EmployeeListView(generics.ListCreateAPIView):
    
    serializer_class=EmployeeSerializer
    
    queryset=Employee.objects.all()
    
class EmployeeGenericView(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class=EmployeeSerializer
    
    queryset=Employee.objects.all()