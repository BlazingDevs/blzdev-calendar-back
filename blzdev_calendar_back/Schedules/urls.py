from django.urls import path
from . import views

urlpatterns = [
    path('<int:schedule_id>/', views.ScheduleDetailAPI),
    path('', views.ScheduleListAPI),
]
