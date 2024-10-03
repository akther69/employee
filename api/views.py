from django.shortcuts import render

from rest_framework.views import APIView

from Myapp.models import Employee,Work

from api.serializers import EmployeeSerializer,WorkSerializer

from rest_framework.response import Response

from rest_framework import viewsets

from rest_framework.decorators import action

from rest_framework import generics

from rest_framework import authentication,permissions

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
    
    authentication_classes=[authentication.BasicAuthentication]
    
    permission_classes=[permissions.IsAuthenticated]
    
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
    
    @action(methods=["POST"],detail=True)
    
    def add_work(self,request,*args, **kwargs):
        
        employee_id=kwargs.get("pk")
        
        employee_obj=Employee.objects.get(id=employee_id)
        
        serializer_instance=WorkSerializer(data=request.data)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save(employee_object=employee_obj)
            
            return Response(data=serializer_instance.data)
        
        return Response(data=serializer_instance.errors)
        
        
    
class EmployeeListView(generics.ListCreateAPIView):
    
    serializer_class=EmployeeSerializer
    
    queryset=Employee.objects.all()
    
class EmployeeGenericView(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class=EmployeeSerializer
    
    queryset=Employee.objects.all()
    
    
class WorkRetrieveUpdateDestroyView(viewsets.ViewSet):
    
    def destroy(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        Work.objects.get(id=id).delete()
        
        data={"message":"deleted"}
        
        return Response(data)
    
    def update(self,request,*args, **kwargs):
        
        work_id=kwargs.get("pk")
        
        work_obj=Work.objects.get(id=work_id)
        
        serializer_instance=WorkSerializer(data=request.data,instance=work_obj)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save()
            
            return Response(data=serializer_instance.data)
        
        return Response(data=serializer_instance.errors)
    
    def retrieve(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        qs=Work.objects.get(id=id)
        
        serializer_instance=WorkSerializer(qs)
        
        return Response(data=serializer_instance.data)
    
class WorkCreateView(generics.CreateAPIView):
    
    serializer_class=WorkSerializer
    
    queryset=Work.objects.all()
    
    def perform_create(self, serializer):
        
        id=self.kwargs.get("pk")
        
        employee_obj=Employee.objects.get(id=id)
        
        serializer.save(employee_object=employee_obj)
    
    
    # Serializer
    
    # apiview
    
    # viewset and routers
    
    # custom_methods
    
    # serializer relations
    
    # ==>nested serializer 
    
    # ==>string related field 
    
    # authentication permission
    
    

    
    