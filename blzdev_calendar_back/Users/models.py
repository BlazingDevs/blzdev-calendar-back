from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Manager(BaseUserManager):
    def create(self, user_id, user_password, user_name):
        if(not user_id):
            raise ValueError("id needed")
        if(not user_password):
            raise ValueError("password needed")
        if(not user_name):
            raise ValueError("name needed")
            
        user=self.model(
            user_id=user_id,
            user_password=user_password
        )

        user.set_password(user_password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    user_id=models.CharField(max_length=30)
    user_password=models.CharField(max_length=30)
    user_name=models.CharField(max_length=100)

    objects = Manager()

    USERNAME_FIELD = 'user_name'

    def __str__(self):
        return self.user_name