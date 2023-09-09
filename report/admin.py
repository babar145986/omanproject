from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import AddRecord

class AddRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_of_contract', 'khaif_no')

admin.site.register(AddRecord, AddRecordAdmin)
