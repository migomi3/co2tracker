from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel
from django.conf import settings


# Create your models here.

# Activity model to track user activities regarding carbon emissions
# Discussed fields include:
# - user: ForeignKey to User model
# electricity_uni[I say we leave it default to kwh], electricity_value, country, state

class Activity(SoftDeletableModel, TimeStampedModel):
    """
    Model to save possible activities related to carbon emissions
    """

    class ActivityTypes(models.TextChoices):
        ELECTRICITY = 'electricity', 'Electricity'
        TRANSPORT = 'transport', 'Transport'
        OTHER = 'other', 'Other'

    class ValueMetrics(models.TextChoices):
        KWH = 'kWh', 'Kilowatt Hour'
        KM = 'km', 'Kilometer'
        OTHER = 'other', 'Other'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=15, choices=ActivityTypes.choices, default=ActivityTypes.OTHER)  # e.g., electricity, transport
    value_metric = models.CharField(max_length=10, choices=ValueMetrics.choices)  # e.g., kWh for electricity, km for transport  (based on activity type)
    value = models.FloatField()
    country = models.CharField(max_length=100, blank=True, null=True)  # Change to choice using library field
    state = models.CharField(max_length=100, blank=True, null=True)    # Change to choice using library field
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} - {self.value} at {self.timestamp}"


class ActivityLog(TimeStampedModel):
    """
    Model to log activities related to carbon emissions.
    Logs can be a different app, but for simplicity, we keep it here.
    """
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='logs')
    description = models.TextField()

    def __str__(self):
        return f"Log for {self.activity} at {self.modified or self.created}"