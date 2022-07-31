from rest_framework import serializers, validators
from .models import User

class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'password', 'user_name')

        extra_kwargs = {
            "user_id": {
                "validators":[
                    validators.UniqueValidator(
                        User.objects.all(),
                        "이미 존재하는 아이디입니다."
                    )
                ]
            },
            "password": {"write_only":True} #write_only를 통해 GET요청 시 접근을 차단
        }

    def create(self, validated_data):
        user_id=validated_data['user_id']
        password=validated_data['password']
        user_name=validated_data['user_name']

        user = User.objects.create_user(
            user_id=user_id,
            password=password,
            user_name=user_name
        )

        return user