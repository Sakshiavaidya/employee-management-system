from django.contrib import admin
from employemodel.models import Employee

class employeAdmin(admin.ModelAdmin):
    list_display=('name','email','address','phone')


admin.site.register(Employee,employeAdmin)# Register your models here.
