from django.contrib import admin
from .models import Guest

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name')
    list_display_links = ('id', 'first_name')


    