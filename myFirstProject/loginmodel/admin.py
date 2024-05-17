from django.contrib import admin
from loginmodel.models import LoginModel

class LoginAdmin(admin.ModelAdmin):
    list_display=('username','password')
    
admin.site.register(LoginModel,LoginAdmin)    

# Register your models here.
