from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.ScheduleDetailAPI.as_view()),
    path('', views.ScheduleListAPI.as_view()),
]
