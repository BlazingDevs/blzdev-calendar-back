from asyncio.windows_events import NULL
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
        # UserQuerySet = User.objects.values_list(
        #     'obj__members_id', flat=True)
        serializer = ScheduleMemberSerializer(obj, many=True)

        # members = {"count": 0, "member": serializer.data}
        members = {"count": 0, "member": NULL}
        print(obj)
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
