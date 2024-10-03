from django.urls import path

from api import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("v1/employees",views.EmployeeViewsetView,basename="employees")

router.register("v1/works",views.WorkRetrieveUpdateDestroyView,basename="works")


urlpatterns = [
    path("employee/",views.EmployeeCreateListView.as_view()),
    
    path("employee/<int:pk>/",views.EmployeeRetrieveUpdateDestroyView.as_view()),
    
    path("v2/employees/",views.EmployeeListView.as_view()),
    
    path("v2/employees/<int:pk>/",views.EmployeeGenericView.as_view()),
    
    path("v2/employees/<int:pk>/works/add/",views.WorkCreateView.as_view())
    
]+router.urls
