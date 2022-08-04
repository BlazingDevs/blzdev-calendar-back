from rest_framework import serializers
from Schedules.models import Schedules
from Users.models import User


class SchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = '__all__'
