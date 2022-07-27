from rest_framework import serializers
from .models import dev_logs
from Schedules.models import Schedules

# class dev_logs(models.Model):
# 	schedule_id = models.ForeignKey(Schedules, on_delete=models.CASCADE) # 일정 id
# 	#user_id = models.ForeignKey(User) # 작성자 id
# 	content = models.CharField(max_length=200) # 개발 일지 내용

class DevLogSerializer(serializers.ModelSerializer):
    schedule_id = serializers.IntegerField(write_only = True)
    class Meta:
        model = dev_logs
        fields = ('schedule_id','content')
        # write_only_fields = ('schedule_id','content')
        # write_only_fields = ('user_id','schedule_id','content')
        # read_onlyfields = ('user_id','content')
    def create(self,validated_data):
        schedule_id = int(validated_data['schedule_id'])
        AllObjects = Schedules.objects.all()
        if AllObjects.filter(id = schedule_id).exists():
            obj = dev_logs.objects.create(**validated_data)
            return obj
        else:
            raise AttributeError

        

    