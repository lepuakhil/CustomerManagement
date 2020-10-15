from django.contrib import admin

# Register your models here.

from .models import *

# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('name','phone','email','date_created')

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)



