from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import DevLogSerializer
from .models import dev_logs

# serializer ID 기반 필드?
# error message 출력 다른 방법? (validators)
# 유저 아이디 입력 구현
#url api 명세 수정 필요

@csrf_exempt
def DevLogs(request): 
    if request.method == 'GET': # url /dev_logs?schedule_id=1
        if not 'schedule_id' in request.GET: #GET url parameter schedule_id 유무 확인
            ResponseData = {"error_code": 404, "error_messsage": "no schedule_id parameter", "data" : ""}
        else:
            schedule_id = request.GET['schedule_id']
            AllObjects = dev_logs.objects.all()

            if not AllObjects.filter(schedule_id = schedule_id).exists(): # schedule_id 유효한지 확인
                ResponseData = {"error_code": 404, "error_messsage": f'no schedule_id {schedule_id} in DB', "data" : ""}
            else:
                serializer = DevLogSerializer(AllObjects.filter(schedule_id = schedule_id),many=True)
                ResponseData = {"error_code": 0,"error_message":"", "data" : serializer.data}

    elif request.method == 'POST': #url /dev_logs
        data = JSONParser().parse(request)
        serializer = DevLogSerializer(data=data)

        if not serializer.is_valid(): #POST JSON 유효성 검사
            ResponseData = {"error_code": 500, "error_message": "unvalid request", "data": ""}
        else:
            try:
                serializer.save()   #dev_log 생성
                ResponseData = {"error_code": 0,"error_message":"", "data" : serializer.data}
            except AttributeError:  #생성 실패시
                ResponseData = {"error_code": 404, "error_messsage": "no schedule id in DB", "data" : ""}
        
    else: # GET, POST 외의 request method
        ResponseData = {"error_code": 404, "error_messsage": "unvalid request method", "data" : ""}

    return JsonResponse(ResponseData,status=200)
    
@csrf_exempt
def DevLog(request,pk):
    if request.method == 'PUT': #url  /dev_logs/{dev_log_id}
        AllObjects = dev_logs.objects.all()

        if not AllObjects.filter(id=pk).exists(): # pk 값 확인
            ResponseData = {"error_code": 404, "error_message": "no log_id in DB", "data" : ""}
        else:
            obj = AllObjects.get(id=pk)
            data = JSONParser().parse(request)
            serializer = DevLogSerializer(obj,data=data)

            if serializer.is_valid(): #유효성 판정
                try:
                    serializer.save()
                    ResponseData = {"error_code":0, "error_message": "", "data": serializer.data}
                except:
                    ResponseData = {"error_code": 404, "error_messsage": "schedule_id change is not allowed", "data" : ""}
            else:
                ResponseData = {"error_code": 500, "error_message": "unvalid request", "data": ""}
    
    elif request.method == 'DELETE':
        AllObjects = dev_logs.objects.all()

        if not AllObjects.filter(id=pk).exists(): #pk 값 확인
            ResponseData = {"error_code": 404, "error_message": "no log_id in DB", "data" : ""}
        else:
            AllObjects.get(id=pk).delete()
            ResponseData = {"error_code": 0, "error_message": ""}
    
    else: #PUT, DELETE 외의 pk 값
        ResponseData = {"error_code": 404, "error_messsage": "unvalid request method", "data" : ""}
    
    return JsonResponse(ResponseData,status=200)