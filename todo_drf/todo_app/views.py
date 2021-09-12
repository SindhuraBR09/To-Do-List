from django.shortcuts import render
from .models import Task
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TaskSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    print("api overview")
    api_urls = {
    'List': '/task-list',
    'Create': '/create-task/',
    'Detail': '/detail-task/<str:pk>',
    'Update': '/update-task/<str:pk>',
    'Delete' : '/delete-task/<str:pk>'
    }

    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):

    tasks = Task.objects.all()
    print("Got all the task objects {}".format(tasks))
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskdetail(request,pk):

    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskcreate(request):

    serializer = TaskSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskupdate(request, pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(instance=task, data = request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskdelete(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return Response("Item deleted!!!!!")
