from rest_framework import serializers
from Schedules.models import Schedules
from Users.models import User

class SchedulesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedules
        fields = ('id', 'schedule_name', 'workspace_id',
                  'date', 'time', 'members_id')