from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import dev_logs
from Schedules.models import Schedules
from Users.models import User

class DevLogSerializer(serializers.ModelSerializer):
    user_id = serializers.SlugRelatedField(slug_field = 'user_id', read_only = True)
    class Meta:
        model = dev_logs
        fields = ('schedule_id','user_id','content')

        

    