from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('objective', 'user', 'deadline', 'completed', 'created_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('objective', 'user__username')
    date_hierarchy = 'deadline'