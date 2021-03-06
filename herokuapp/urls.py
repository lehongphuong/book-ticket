from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    # *******************************************************	
    # begin Customer	
    path('createDataCustomer', views.createDataCustomer, name='createDataCustomer'), 	
    path('readDataCustomer', views.readDataCustomer, name='readDataCustomer'), 	
    path('updateDataCustomer', views.updateDataCustomer, name='updateDataCustomer'), 	
    path('deleteDataCustomer', views.deleteDataCustomer, name='deleteDataCustomer'),  	
    path('findDataCustomer', views.findDataCustomer, name='findDataCustomer'),  	
    path('find_custommer_by_status', views.find_custommer_by_status, name='find_custommer_by_status'),  	
    # end Customer	
    # *******************************************************	 
]
