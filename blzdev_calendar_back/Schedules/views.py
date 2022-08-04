from django.shortcuts import render
# from django.views import View
from django.views.generic import DetailView
from Schedules.models import *

from Schedules.serializers import SchedulesSerializer
# from accounts.models import Users
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# @api_view(['GET', 'PUT', 'DELETE'])
# def patch_delete(request):
#     if request.method == 'PATCH':
#         user = get_object_or_404(models.User, user=request.user)
#         # partial=True이므로 PATCH method가 가능함
#         serializer = UserSerializer(user, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         # auth의 User가 삭제되면 Model의 User 또한 삭제됨 (CASCADE)
#         user = get_object_or_404(User, id=request.user.id)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
