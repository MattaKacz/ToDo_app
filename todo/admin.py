from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'created_at',
                    'updated_at', 'due_date')
    search_fields = ('task',)

admin.site.register(Task, TaskAdmin)
