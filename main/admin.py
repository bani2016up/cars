from django.contrib import admin
from main.models import *
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('model',)}
    
admin.site.register(Car, CarAdmin)