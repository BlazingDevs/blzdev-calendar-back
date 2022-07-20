from django.db import models

# Create your models here.
class Workspace(models.Model):
    workspace_name = models.CharField(max_length=100) #workspace 이름

