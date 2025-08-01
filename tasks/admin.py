# tasks/admin.py

from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created_at')
    list_filter = ('completed',)
    search_fields = ('title',)
