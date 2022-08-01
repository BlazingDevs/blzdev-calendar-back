from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.DevLogs),
    path('<int:pk>/',views.DevLog),
]