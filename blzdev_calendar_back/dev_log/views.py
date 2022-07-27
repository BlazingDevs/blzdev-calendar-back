from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import DevLogSerializer
from .models import dev_logs

@csrf_exempt
def index(request): 
    if request.method == 'GET':
        schedule_id = request.GET['schedule_id']
        AllObjects = dev_logs.objects.all()
        # if AllObjects.filter(schedule_id = schedule_id).exists():
        serializer = DevLogSerializer(AllObjects.filter(schedule_id = schedule_id),many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DevLogSerializer(data=data)

        if serializer.is_valid(): #유효성 검사
            try:
                serializer.save()   #dev_log 생성
                ResponseData = {"error_code": 0,"error_message":"", "data" : serializer.data}
            except AttributeError:  #생성 실패시
                ResponseData = {"error_code": 404, "error_messsage": "no schedule id", "data" : ""}
        else:
            ResponseData = {"error_code": 500, "error_message": "unvalid request", "data": ""}
        
        return JsonResponse(ResponseData,status=200)

