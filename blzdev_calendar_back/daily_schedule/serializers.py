from rest_framework import serializers
from Schedules.models import Schedules

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = ('id', 'schedule_name', 'time')