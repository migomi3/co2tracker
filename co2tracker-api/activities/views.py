from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Activity, ActivityLog
from .serializers import ActivitySerializer, ActivityLogSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Activity instances.
    """
    serializer_class = ActivitySerializer
    permission_classes = (IsAuthenticated,)
    queryset = Activity.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['activity_type', 'value_metric', 'country', 'state']
    search_fields = ['activity_type', 'country', 'state']
    ordering_fields = ['timestamp', 'value', 'created', 'modified']
    
    def get_queryset(self):
        """
        This view should return a list of all activities
        for the currently authenticated user.
        """
        return Activity.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """
        Set the user to the current user when creating a new activity
        """
        serializer.save(user=self.request.user)


class ActivityLogViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing ActivityLog instances.
    """
    serializer_class = ActivityLogSerializer
    permission_classes = (IsAuthenticated,)
    queryset = ActivityLog.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['activity']
    search_fields = ['description']
    ordering_fields = ['created', 'modified']
    
    def get_queryset(self):
        """
        This view should return a list of all activity logs
        for the currently authenticated user's activities.
        """
        return ActivityLog.objects.filter(activity__user=self.request.user)
