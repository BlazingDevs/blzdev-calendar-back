from rest_framework import serializers
from Schedules.models import Schedules
from Users.models import User


class SchedulesSerializer(serializers.ModelSerializer):
    # count_members = users.objects.annotate(dep_count=Count('employee')).count()
    class Meta:
        model = Schedules
        exclude = ('users', )
        # fields = '__all__'

# class ScheduleMemberSerializer(serializers.ModelSerializer):
#     def get_members(self,instance):
#         result = dict()
    
#         user_schedule = UserWorkspaces.objects.filter(workspace__id=instance.id).values_list('user__user_primary_id',flat=True)
#         result['count'] = users.count()
#         result['member'] = WorkspaceUserSerializer(User.objects.filter(user_primary_id__in=user_schedule),many=True).data
        
#         return result
    
#     schedule_id = serializers.ReadOnlyField(source='id')
#     members = serializers.SerializerMethodField()
