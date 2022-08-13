from Schedules.models import *
from Schedules.serializers import SchedulesSerializer
from rest_framework import generics, mixins

class ScheduleDetailAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = SchedulesSerializer
    queryset = Schedules.objects.all()
    lookup_field = 'id'
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ScheduleListAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = SchedulesSerializer
    queryset = Schedules.objects.all()

    def get_queryset(self):
        workspaces_id = self.request.GET['workspace']
        date = self.request.GET['date']
        return Schedules.objects.filter(workspace_id__exact=workspaces_id, date__exact=date)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
