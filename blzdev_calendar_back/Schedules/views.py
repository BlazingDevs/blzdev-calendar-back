from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from Schedules.models import *
from Schedules.serializers import SchedulesSerializer


@csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
@api_view(['GET'])
def schedule_detail(request, schedule_id=None):
    schedule = get_object_or_404(Schedules, id=schedule_id)
    response_data = {'error_code': -1, 'error_message': None, 'data': None}

    if request.method == 'GET':
        response_data['error_message'] = 'get schedule'
        response_data['data'] = SchedulesSerializer(schedule).data

    else:
        response_data['error_code'] = 400
        response_data['error_message'] = 'unvalid request method'

    return Response(response_data)


@api_view(['PUT'])
def put_schedule_detail(request, schedule_id=None):
    schedule = get_object_or_404(Schedules, id=schedule_id)
    response_data = {'error_code': -1, 'error_message': None, 'data': None}

    if request.method == 'PUT':
        serializer = SchedulesSerializer(schedule, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            
        response_data['error_code'] = 200
        response_data['error_message'] = 'put schedule'

    return Response(response_data)


@api_view(['DELETE'])
def delete_schedule_detail(request, schedule_id=None):
    schedule = get_object_or_404(Schedules, id=schedule_id)
    response_data = {'error_code': -1, 'error_message': None, 'data': None}

    if request.method == 'DELETE':
        schedule.delete()

        response_data['error_code'] = 200
        response_data['error_message'] = 'Delete schedule'

    return Response(response_data)
