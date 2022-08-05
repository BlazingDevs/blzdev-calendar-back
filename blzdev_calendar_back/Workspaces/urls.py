from django.urls import path
from .views import *


urlpatterns = [
    path('', workspaces),
    path('<int:pk>', workspace_detail),
]