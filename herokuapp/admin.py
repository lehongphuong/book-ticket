from django.contrib import admin

# Register your models here.
from . import models

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','cmnd','username','phone','number_ticket','deposit','money','start_date','start_time_train','end_date','end_time_train','note','status')
    list_filter = ['id','cmnd','username','phone','number_ticket','deposit','money','start_date','start_time_train','end_date','end_time_train','note','status']
    search_fields = ['id','cmnd','username','phone','number_ticket','deposit','money','start_date','start_time_train','end_date','end_time_train','note','status'] 
 
admin.site.register(models.Customer, CustomerAdmin)
