from django.contrib import admin
from .models import Emp
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working', 'emp_id')
    #list_editable=('working', 'phone')
    search_fields=('name', 'address')
    list_filter=('address','working')

admin.site.register(Emp, EmpAdmin)