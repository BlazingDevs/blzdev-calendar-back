from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Manager(BaseUserManager):
    def create_user(self, user_id, user_name, password=None):

        user = self.model(
            user_id=user_id,
            user_name=user_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_primary_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=30, unique=True)
    user_name = models.CharField(max_length=100)

    objects = Manager()

    USERNAME_FIELD = 'user_id'

    def __str__(self):
        return self.user_name
