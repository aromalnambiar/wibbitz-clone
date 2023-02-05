from django.contrib import admin
from web.models import Customers, Subscriber


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id","name","image"]

admin.site.register(Customers,CustomerAdmin)

admin.site.register(Subscriber)
