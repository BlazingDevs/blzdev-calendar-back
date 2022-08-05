from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import WorkspaceDetailSerializer,UserWorkspaceSerializer
from .models import Workspaces,UserWorkspaces
from Users.models import User



@api_view(['GET','POST'])
def workspaces(request):
    
    res_data = dict()
    res_data['error_code']=0
    res_data['error_message'] = ''
    
    res_data['data']=dict()
    
    if request.method == 'GET':
        print(request.user)
        user_workspaces = UserWorkspaces.objects.filter(user=request.user)
        
        work_spaces = dict()
        work_spaces['count'] = user_workspaces.count()
        work_spaces['work_space'] =UserWorkspaceSerializer(user_workspaces,many=True).data
        
        res_data['data']['work_spaces'] = work_spaces
    
    elif request.method == 'POST':
        
        data = request.data
        
        workspace = Workspaces.objects.create(
            workspace_name=data['workspace_name']
        )
        for i in data['members_id']:
            UserWorkspaces.objects.create(
                user = User.objects.get(user_primary_id=i),
                workspace=workspace
            )
        res_data['data'] = {'workspace_id':workspace.id}
        
    return Response(res_data)


@api_view(['GET','PUT','DELETE'])
def workspace_detail(request,pk=None):
        
    res_data = dict()
    res_data['error_code']=0
    res_data['error_message'] = ''
    
    res_data['data']=dict()
    if Workspaces.objects.filter(id=pk).exists():
        if request.method == 'GET':
            workspace = Workspaces.objects.get(id=pk)
            res_data['data']['members']=WorkspaceDetailSerializer(workspace).data
        elif request.method == 'PUT':
            data = request.data
            UserWorkspaces.objects.filter(workspace__id=pk).delete()
            workspace = Workspaces.objects.get(id=pk)
            for i in data['members_id']:
                UserWorkspaces.objects.create(
                    user = User.objects.get(user_primary_id=i),
                    workspace=workspace
                )
            
            res_data['data'] = {'workspace_id':workspace.id}
            
        elif request.method == 'DELETE':
            Workspaces.objects.filter(id=pk).delete()
    return Response(res_data)