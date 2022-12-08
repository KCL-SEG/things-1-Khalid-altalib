from django.contrib import admin
"""Configuration of Admin interface for things app."""
# Register your models here.
from django.contrib import admin
from .models import Thing
@admin.register(Thing)
class ThingAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'quantity')
    list_filter = ('name', 'description', 'quantity')
    search_fields = ('name', 'description', 'quantity')
    ordering = ('name', 'description', 'quantity')

