from django.db import models
from api.Workspaces.models import Workspaces

class Schedules(models.Model):
	schedule_name = models.CharField(max_length=100) # 일정 이름
	workspace_id = models.ForeignKey(Workspaces, on_delete = models.CASCADE) # 워크스페이스 고유 ID
	start_date = models.CharField(max_length=10) # 시작 날짜
	end_date = models.CharField(max_length=10) # 종료 날짜
	time = models.FloatField() # 진행 시간