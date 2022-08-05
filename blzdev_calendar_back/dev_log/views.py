from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import DevLogSerializer
from .models import dev_logs
from Schedules.models import Schedules
from rest_framework.decorators import api_view


# error message 출력 다른 방법? (validators)

@csrf_exempt
@api_view(['GET','POST','PUT','DELETE'])
def DevLogs(request): 
    if request.method == 'GET': # url /dev_logs?schedule_id=1
        if not 'schedule_id' in request.GET: #GET url parameter schedule_id 유무 확인
            ResponseData = {"error_code": 404, "error_messsage": "no schedule_id parameter", "data" : ""}
        else:
            schedule_id = request.GET['schedule_id']
            LogQuerySet = dev_logs.objects.filter(schedule_id = schedule_id)
            serializer = DevLogSerializer(LogQuerySet,many=True)
            ResponseData = {"error_code": 0, "error_message":"", "data" : serializer.data}

    elif request.method == 'POST': #url /dev_logs 
        data = JSONParser().parse(request)
        schedule_id = int(data['schedule_id'])
        SchedulesQuerySet = Schedules.objects.all()

        if not SchedulesQuerySet.filter(id = schedule_id).exists(): #request data schedule_id 검사
            ResponseData = {"error_code": 404, "error_messsage": "there is no schedule_id in DB}", "data" : ""}
        else:
            LogQuerySet = dev_logs.objects.filter(schedule_id = schedule_id)
            if LogQuerySet.filter(user_id = request.user).exists(): # 이미 log 작성했는지 검사
                ResponseData ={"error_code": 404, "error_messsage": "user already writes dev_log in this schedule", "data" : "" }
            else:
                newDevLog = LogQuerySet.create(
                    schedule_id = SchedulesQuerySet.get(id = int(data['schedule_id'])),
                    content = data['content'],
                    user_id = request.user)
                newDevLog.save()
                serializer = DevLogSerializer(newDevLog)
                ResponseData ={"error_code": 200, "error_messsage": "", "data" : serializer.data }

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        schedule_id = int(data['schedule_id'])
        SchedulesQuerySet = Schedules.objects.all()

        if not SchedulesQuerySet.filter(id = schedule_id).exists(): #request data schedule_id 검사
            ResponseData = {"error_code": 404, "error_messsage": "there is no schedule_id in DB}", "data" : ""}
        else:
            LogQuerySet = dev_logs.objects.filter(schedule_id = schedule_id)
            if not LogQuerySet.filter(user_id = request.user).exists(): #이미 로그 작성했는지 검사
                ResponseData ={"error_code": 404, "error_messsage": "user didn't write dev_log in this schedule", "data" : "" }
            else:
                myDevLog = LogQuerySet.get(user_id = request.user)
                myDevLog.content = data['content']
                myDevLog.save()
                serializer = DevLogSerializer(myDevLog)
                ResponseData ={"error_code": 200, "error_messsage": "", "data" : serializer.data }

    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        schedule_id = int(data['schedule_id'])
        SchedulesQuerySet = Schedules.objects.all()

        if not SchedulesQuerySet.filter(id = schedule_id).exists(): #request data schedule_id 검사
            ResponseData = {"error_code": 404, "error_messsage": "there is no schedule_id in DB}", "data" : ""}
        else:
            LogQuerySet = dev_logs.objects.filter(schedule_id = schedule_id)
            if not LogQuerySet.filter(user_id = request.user).exists(): #이미 로그 작성했는지 검사
                ResponseData ={"error_code": 404, "error_messsage": "user didn't write dev_log in this schedule", "data" : "" }
            else:
                LogQuerySet.get(user_id = request.user).delete()
                ResponseData ={"error_code": 200, "error_messsage": "", "data" : ""}

    else: # GET, POST, PUT, DELETE 외의 request method
        ResponseData = {"error_code": 404, "error_messsage": "unvalid request method", "data" : ""}

    return JsonResponse(ResponseData,status=200)