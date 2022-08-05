from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from Users.models import User
from .serializers import ScheduleSerializer
from Schedules.models import Schedules

# Create your views here.
@api_view(['GET'])
def daily_schedule(request):
    if request.method == 'GET':
        if not 'date' in request.GET:
            ResponseData = {"error_code" : 404, "error_message" : "there is no date in query", "data" : ""}
        else:
            date = request.GET['date']
            ScheduleQuerySet = Schedules.objects.filter(date = date)
            serializer = ScheduleSerializer(ScheduleQuerySet,many=True)
            ResponseData = {"error_code" : 200, "error_message" : "", "data" : {"count" : len(ScheduleQuerySet), "schedule" : serializer.data}}
    return JsonResponse(ResponseData, status=200)