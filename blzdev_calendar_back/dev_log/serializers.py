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
        fields = ('id','schedule_id','content')
        
    def create(self,validated_data):
        schedule_id = validated_data.pop('schedule_id')
        AllObjects = Schedules.objects.all()
        
        if AllObjects.filter(id = schedule_id).exists():
            schedule = AllObjects.get(id = schedule_id)
            obj = dev_logs.objects.create(**validated_data,schedule_id = schedule)
            return obj
        else:
            raise AttributeError

    def update(self,instance, validated_data):
        if instance.schedule_id.id != int(validated_data['schedule_id']): #content외에 다른 정보 수정 시
            raise AttributeError
        else:
            instance.content = validated_data['content']
            instance.save()
            return instance

        

    