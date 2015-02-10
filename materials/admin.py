from django.contrib import admin
from materials.models import *

class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('date', 'job', 'vendor', 'amount', 'createduser')

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email')

# Register your models here.
admin.site.register(Company)
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(JobPhases)
admin.site.register(Jobs)
admin.site.register(Vendors)
admin.site.register(Materials, MaterialsAdmin)
'''
admin.site.register(xxx)
admin.site.register(xxx)
admin.site.register(xxx)
admin.site.register(xxx)
admin.site.register(xxx)
'''