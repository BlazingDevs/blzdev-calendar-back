from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from Schedules.models import *
from Schedules.serializers import SchedulesSerializer
from rest_framework import generics, mixins

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def schedule_detail(request, schedule_id=None):
    schedule = get_object_or_404(Schedules, id=schedule_id)
    response_data = {'error_code': -1, 'error_message': None, 'data': None}

    if request.method == 'GET':
        response_data['error_message'] = 'get schedule'
        response_data['data'] = SchedulesSerializer(schedule).data

    elif request.method == 'PUT':
        serializer = SchedulesSerializer(schedule, data=request.data)

        if serializer.is_valid():
            serializer.save()

        response_data['error_code'] = 200
        response_data['error_message'] = 'put schedule'

    elif request.method == 'DELETE':
        schedule.delete()

        response_data['error_code'] = 200
        response_data['error_message'] = 'Delete schedule'
    else:
        response_data['error_code'] = 400
        response_data['error_message'] = 'unvalid request method'

    return Response(response_data)

class ScheduleListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = SchedulesSerializer
    def get_queryset(self):
        workspaces_id = self.request.GET['workspace']
        date = self.request.GET['date']
        print(workspaces_id)
        print(11111)
        print(date)
        return Schedules.objects.filter(workspace_id_id__exact=workspaces_id, date__exact=date)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)