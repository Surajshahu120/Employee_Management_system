from django.contrib import admin
from .models import Employees_table
from .models import Role
from .models import Department


class Employees_table_data(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "dept", "salary",
                    "bonus", "role", "Phone", "hire_date")
    
admin.site.register(Employees_table,Employees_table_data)
admin.site.register(Role) 
admin.site.register(Department) 


# Register your models here.
