from rest_framework import serializers
from .models import Workspaces,UserWorkspaces
from Users.models import User

class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspaces
        fields = ('id','workspace_name',)
        
class UserWorkspaceSerializer(serializers.ModelSerializer):
    workspace_name = serializers.ReadOnlyField(source='workspace.workspace_name')
    
    class Meta:
        model = UserWorkspaces
        fields = ('workspace_id','workspace_name',)
        
class WorkspaceUserSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_primary_id')
    class Meta:
        model = User
        fields = ('user_id','user_name',)


class WorkspaceDetailSerializer(serializers.ModelSerializer):
    workspace_id = serializers.ReadOnlyField(source='id')
    members = serializers.SerializerMethodField()
    
    def get_members(self,instance):
        result = dict()
        user_workspace = UserWorkspaces.objects.filter(workspace__id=instance.id).values_list('user__user_primary_id',flat=True)
        result['count'] = user_workspace.count()
        result['member'] = WorkspaceUserSerializer(User.objects.filter(user_primary_id__in=user_workspace),many=True).data
        return result
        
    
    
    class Meta:
        model = Workspaces
        fields = ('workspace_id','workspace_name','members')