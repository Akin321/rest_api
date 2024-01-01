from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView
from .serializers import TaskSerializers,UserSerializers
from .models import Task
# Create your views here.

class TaskViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset=Task.objects.all().order_by('date_created')
    serializer_class = TaskSerializers
class DueTaskViewset(viewsets.ModelViewSet):
    queryset=Task.objects.all().order_by('date_created').filter(complete=False)
    serializer_class = TaskSerializers
class CompletedTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('date_created').filter(complete=True)
    serializer_class = TaskSerializers
class CreateuserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializers


