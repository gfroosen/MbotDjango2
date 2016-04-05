from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from portal.models import Robot
from api.serializers import RobotSerializer
from django.http import HttpResponse
from django.shortcuts import render
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404



@api_view(['GET', 'POST','DELETE'])
def api_dashboard(request):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        tasks = Robot.objects.all()
        serializer = RobotSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RobotSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def api_detail(request, pk):
    """
    Get, udpate, or delete a specific task
    """
    try:
        task = Robot.objects.get(pk=pk)
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RobotSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RobotSerializer(task, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



def index(request):
    return render(request, 'index.html', {})


def robot_control(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.controler=request.user
            post.save()

    else:
        form = PostForm()
    return render(request, 'api/robot_control.html', {'form': form})


def robot_detail(request,pk):
    form = get_object_or_404(Robot, pk=pk)

    return render(request, 'api/robot_detail.html', {'form': form})

def robot_edit(request, pk):
    form = get_object_or_404(Robot, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=form)
        if form.is_valid():
            post = form.save(commit=False)
            post.controler = request.user
            post.published_date = timezone.now()
            post.save()
        return render(request, 'api/robot_detail.html', {'form': form})

    else:
        form = PostForm(instance=form)
    return render(request, 'api/robot_edit.html', {'form': form})
