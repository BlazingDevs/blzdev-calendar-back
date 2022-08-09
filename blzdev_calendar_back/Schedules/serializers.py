from rest_framework import serializers
from Schedules.models import Schedules, User_Schedule
from Users.models import User


class ScheduleMemberSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_primary_id')

    class Meta:
        model = User
        fields = ('user_id', 'user_name')


class SchedulesSerializer(serializers.ModelSerializer):
    # Schedules 모델에 없는 새로운 members field를 추가함.
    members = serializers.SerializerMethodField()

    class Meta:
        model = Schedules
        fields = '__all__'
        fields = ('id', 'schedule_name', 'workspace_id',
                  'date', 'time', 'members')

    def get_members(self, obj):
        members = {}

        user_schedule = User_Schedule.objects.filter(
            schedule_id=obj.id).values_list('user_id', flat=True)

        members['count'] = user_schedule.count()
        members['member'] = ScheduleMemberSerializer(
            User.objects.filter(user_primary_id__in=user_schedule), many=True).data

        return members
