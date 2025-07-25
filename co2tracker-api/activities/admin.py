from django.contrib import admin
from .models import Activity, ActivityLog


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'activity_type', 'value_metric', 'value', 'country', 'state', 'timestamp')
    list_filter = ('activity_type', 'value_metric', 'country', 'state', 'timestamp')
    search_fields = ('user__username', 'country', 'state')
    date_hierarchy = 'timestamp'
    readonly_fields = ('created', 'modified')


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'activity', 'description', 'created', 'modified')
    list_filter = ('created', 'modified')
    search_fields = ('description', 'activity__user__username')
    readonly_fields = ('created', 'modified')
