from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel')
    list_display_links = ('id', 'hotel')
