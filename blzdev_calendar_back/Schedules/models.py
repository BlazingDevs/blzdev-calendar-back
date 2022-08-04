from django.db import models
from Workspaces.models import Workspaces
from Users.models import User


class Schedules(models.Model):
    # id 자동 생성
    schedule_name = models.CharField(max_length=100)  # 일정 이름
    end_date = models.DateField()  # 종료 날짜
    time = models.FloatField()  # 진행 시간
    users = models.ManyToManyField(
        "User", related_name="User_Schedule")  # Users-Schedules 다대다
