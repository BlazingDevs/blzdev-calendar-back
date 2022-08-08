from django.urls import path
from . import views

urlpatterns = [
    path('<int:schedule_id>/', views.schedule_detail, name='schedule'),
    # TODO: path 설정 /schedules?workspace_id={workspace_id}&&date={date}'
]
