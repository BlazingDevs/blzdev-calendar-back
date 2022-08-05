from django.db import models


class Workspaces(models.Model):
    workspace_name = models.CharField(max_length=100) #workspace 이름
    

class UserWorkspaces(models.Model):
    user = models.ForeignKey('Users.User',on_delete = models.CASCADE)
    workspace = models.ForeignKey('Workspaces',on_delete = models.CASCADE)