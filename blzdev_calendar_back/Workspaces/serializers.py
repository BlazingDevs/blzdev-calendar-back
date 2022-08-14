from rest_framework import serializers
from .models import Workspaces
from Users.models import User

class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspaces
        fields = ('id','workspace_name',)
        
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
        result['count'] = instance.user_workspace.count()
        result['member'] = instance.user_workspace.values('user_id','user_name')
        
        return result
        
    
    
    class Meta:
        model = Workspaces
        fields = ('workspace_id','workspace_name','members')