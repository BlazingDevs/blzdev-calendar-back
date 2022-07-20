from django.db import models
from api.Schedules.models import Schedules
#from api.User.models import User
class dev_logs(models.Model):
	schedule_id = models.ForeignKey(Schedules, on_delete=models.CASCADE) # 일정 id
	#user_id = models.ForeignKey(User) # 작성자 id
	content = models.CharField(max_length=200) # 개발 일지 내용