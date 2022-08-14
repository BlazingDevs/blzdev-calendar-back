from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from Schedules.models import *
from Workspaces.models import *
from Users.models import *
from Schedules.serializers import SchedulesSerializer, SchedulesListSerializer, SchedulesGetSerializer
from rest_framework.response import Response
import json


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def ScheduleDetailAPI(request, schedule_id=None):
    # default response_data
    response_data = {'error_code': -1, 'error_message': None, 'data': None}

    # 존재하는 schedule인지 확인
    try:
        schedule = Schedules.objects.get(id=schedule_id)
    except Schedules.DoesNotExist:
        response_data['error_code'] = 404
        response_data['error_message'] = 'non-exist schedule_id'

        return Response(response_data)

    if request.method == 'GET':
        serializer = SchedulesGetSerializer(schedule)

        response_data['error_code'] = 200
        response_data['error_message'] = 'get schedule'
        response_data['data'] = serializer.data

    elif request.method == 'PUT':
        serializer = SchedulesSerializer(schedule, data=request.data)

        # request 형식이 올바른지 확인
        if serializer.is_valid():
            new_schedule = serializer.save()

            response_data['error_code'] = 200
            response_data['error_message'] = 'put schedule'
            response_data['data'] = {"schedule_id": new_schedule.id}
        else:
            response_data['error_code'] = 401
            response_data['error_message'] = 'serialization is unvalid'
            response_data['data'] = {"schedule_id": new_schedule.id}

    elif request.method == 'DELETE':
        schedule.delete()

        response_data['error_code'] = 200
        response_data['error_message'] = 'Delete schedule'

    # GET, PUT, DELETE 외의 method
    else:
        response_data['error_code'] = 404
        response_data['error_message'] = 'unvalid request method'

    return Response(response_data)


@api_view(['GET', 'POST'])
def ScheduleListAPI(request):
    response_data = {'error_code': -1, 'error_message': None, 'data': None}

    if request.method == 'GET':
        workspace_id = request.GET['workspace']
        date = request.GET['date']

        # 존재하지 않는 workspace인 경우
        if not Workspaces.objects.filter(id=workspace_id).exists():
            response_data['error_code'] = 401
            response_data['error_message'] = 'non-exist workspace'

            return Response(response_data)

        ScheduleQuerySet = Schedules.objects.filter(
            workspace_id__exact=workspace_id, date__exact=date)
        serializer = SchedulesListSerializer(ScheduleQuerySet, many=True)

        response_data['error_code'] = 200
        response_data['error_message'] = 'get schedules'
        response_data['data'] = {"count": len(
            ScheduleQuerySet), "schedule": serializer.data}

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = SchedulesSerializer(data=request.data)

        # workspace가 존재하지 않을 경우
        if not Workspaces.objects.filter(id=request.GET['workspace']).exists():
            response_data['error_code'] = 401
            response_data['error_message'] = 'non-exist workspace'

            return Response(response_data)

        # 존재하지 않는 member_id가 있을 경우
        if len(User.objects.filter(user_primary_id__in=data['members_id'])) != len(data['members_id']):
            response_data['error_code'] = 401
            response_data['error_message'] = 'non-exist member in members_id'

            return Response(response_data)

        # request 형식이 올바른지 확인
        if serializer.is_valid():
            new_schedule = serializer.save()

            response_data['error_code'] = 200
            response_data['error_message'] = 'post schedule'
            response_data['data'] = {"schedule_id": new_schedule.id}
        else:
            response_data['error_code'] = 401
            response_data['error_message'] = 'serialization is unvalid'

    # GET, POST 외의 method
    else:
        response_data['error_code'] = 404
        response_data['error_message'] = 'unvalid request method'

    return Response(response_data)
