from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from . import models

class CustomerAdmin(ImportExportModelAdmin):
    list_display = ('id','cmnd','username','phone','number_ticket','deposit','money','create_date','start_date','start_time_train','end_date','end_time_train','note','status')
    list_filter = ['id','cmnd','username','phone','number_ticket','deposit','money','create_date','start_date','start_time_train','end_date','end_time_train','note','status']
    search_fields = ['id','cmnd','username','phone','number_ticket','deposit','money','create_date','start_date','start_time_train','end_date','end_time_train','note','status'] 
 
admin.site.register(models.Customer, CustomerAdmin)
