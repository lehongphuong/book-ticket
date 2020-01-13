from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    # *******************************************************	
    # begin customer	
    path('createDatacustomer', views.createDatacustomer, name='createDatacustomer'), 	
    path('readDatacustomer', views.readDatacustomer, name='readDatacustomer'), 	
    path('updateDatacustomer', views.updateDatacustomer, name='updateDatacustomer'), 	
    path('deleteDatacustomer', views.deleteDatacustomer, name='deleteDatacustomer'),  	
    path('findDatacustomer', views.findDatacustomer, name='findDatacustomer'),  	
    # end customer	
    # *******************************************************	 
]
