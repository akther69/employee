from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    salary=models.BigIntegerField()
    designation=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    place=models.CharField(max_length=30,null=True)
    
    
    @property
    def works(self):
        
        return Work.objects.filter(employee_object=self)
    
    @property
    def work_count(self):
        
        return self.works.count()
    
    # model string representation
    def __str__(self):
        return self.name
    
    
class Work(models.Model):
    
    employee_object=models.ForeignKey(Employee,on_delete=models.CASCADE)
    
    title=models.CharField(max_length=100)
    
    description=models.CharField(max_length=100)
    
    start_date=models.DateField()
    
    end_date=models.DateField()
    
    status_options=(
        ("created","created"),
        ("wip","wip"),
        ("completed","completed"),
        ("due","due")
    )
    
    status=models.CharField(max_length=200,choices=status_options,default="created")
    
    
    def __str__(self):
        return self.title