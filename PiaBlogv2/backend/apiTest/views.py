from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apiTest.serializers import UserSerializer, GroupSerializer, TaskSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Task

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TaskViewSet(viewsets.ModelViewSet): # Create a class based view
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all() # Select all taks
    serializer_class = TaskSerializer # Serialize data