from rest_framework import serializers
from .models import Activity, ActivityLog


class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = ('id', 'activity', 'description', 'created', 'modified')
        read_only_fields = ('created', 'modified')


class ActivitySerializer(serializers.ModelSerializer):
    logs = ActivityLogSerializer(many=True, read_only=True)
    
    class Meta:
        model = Activity
        fields = ('id', 'user', 'activity_type', 'value_metric', 'value', 
                  'country', 'state', 'timestamp', 'created', 'modified', 'logs')
        read_only_fields = ('created', 'modified', 'timestamp')