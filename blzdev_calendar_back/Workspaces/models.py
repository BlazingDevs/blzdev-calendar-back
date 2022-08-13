from django.db import models


class Workspaces(models.Model):
    workspace_name = models.CharField(max_length=100) # workspace 이름
    user_workspace = models.ManyToManyField('Users.User', related_name= "user_workspaces")