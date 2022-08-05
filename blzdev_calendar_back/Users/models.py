from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Manager(BaseUserManager):
    def create_user(self, user_id, user_name, password=None):
            
        user=self.model(
            user_id=user_id,
            user_name=user_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, user_name, password=None):
        user = self.create_user(
            user_id = user_id,
            user_name=user_name,
            password=password
        )

        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_primary_id = models.AutoField(primary_key=True)
    user_id=models.CharField(max_length=30, unique=True)
    user_name=models.CharField(max_length=100)

    objects = Manager()

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = Manager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name