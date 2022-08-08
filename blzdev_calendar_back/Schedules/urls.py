from django.urls import path
from . import views

urlpatterns = [
    path('<int:schedule_id>/', views.schedule_detail, name='schedule'),
    # delete, put method 를 못 찾아서 일단 url를 나눠 get으로 받아옴
    path('<int:schedule_id>/delete', views.delete_schedule_detail, name='schedule'),
    path('<int:schedule_id>/put', views.put_schedule_detail, name='schedule'),
    # TODO: path 설정 /schedules?workspace_id={workspace_id}&&date={date}'
]
