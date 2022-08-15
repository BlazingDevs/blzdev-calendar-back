#from asyncio.windows_events import NULL
from rest_framework import serializers
from Schedules.models import Schedules
from Users.models import User


class SchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = ('id', 'schedule_name', 'workspace_id',
                  'date', 'time', 'members_id')


class ScheduleMemberSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_primary_id')

    class Meta:
        model = User
        fields = ('user_id', 'user_name')


class SchedulesGetSerializer(serializers.ModelSerializer):
    # Schedules 모델에 없는 새로운 members field를 추가함.
    members = serializers.SerializerMethodField()

    def get_members(self, obj):
        member_queryset = obj.members_id.all()
        members = {"count": member_queryset.count(), "member": ScheduleMemberSerializer(
            member_queryset, many=True).data}

        return members

    class Meta:
        model = Schedules
        fields = ('id', 'schedule_name', 'workspace_id',
                  'date', 'time', 'members')


class SchedulesListSerializer(serializers.ModelSerializer):
    schedule_id = serializers.ReadOnlyField(source='id')

    class Meta:
        model = Schedules
        fields = ('workspace_id', 'schedule_id', 'schedule_name', 'date')
