from django.db import models
from Workspaces.models import Workspaces
from Users.models import User


class Schedules(models.Model):
    # id 자동 생성
    schedule_name = models.CharField(max_length=100)  # 일정 이름
    date = models.DateField(null=True)  # 날짜
    time = models.FloatField(null=True)  # 진행 시간
    workspace_id = models.ForeignKey(Workspaces,on_delete=models.CASCADE)  # 워크스페이스 고유 ID
    members_id = models.ManyToManyField(User, related_name='schedules')
 
    def __str__(self):
        return f"{self.id}"


# class User_Schedule(models.Model):
#     user = models.ForeignKey('Users.User', on_delete=models.CASCADE)
#     schedule = models.ForeignKey('Schedules', on_delete=models.CASCADE)
