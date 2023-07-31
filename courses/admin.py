from django.contrib import admin

# Register your models here.
from .models import AddressInfo


class AddressAdmin(admin.ModelAdmin):
    fields = ["address", "pid"]


admin.site.register(AddressInfo, AddressAdmin)
