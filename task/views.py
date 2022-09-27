from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from rest_framework import status

from task.serializer import  TaskSerializer
from user.utils import Manager_required, admin_required
from user.models import User
from .models import Task
# Create your views here.

class TaskView(APIView):
    serializer_class = TaskSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [Manager_required]
    
    def post(self, request, id=None):
        user = request.data.get('user')
        if user == str(request.user.id): 
            return Response(({'message': 'you can not assign task by own'}))
        is_admin = User.objects.get(id=user)
        if is_admin.role=="admin":
            return Response(({'message': 'you can not assign task to admin'}))
        request.data["manager"] = request.user.id
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
        
    def patch(self, request, id=None):
        try:
            task = Task.objects.get(id=id)
            serializer = self.serializer_class(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
            return Response(serializer.errors)
        except:
            return Response(({'message' : 'Details not found'}), status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, id=None):
        task = Task.objects.get(id=id)
        task.delete()
        return Response(({'message': 'task is deleted successfully'}), status=status.HTTP_204_NO_CONTENT)
                
                
class CheckTaskView(APIView):
    serializer_class = TaskSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [admin_required]
    
    def get(self, request, id=None):
        task = Task.objects.all()
        manager = request.GET.get('manager', None)
        if manager is not None:
            task = task.filter(manager=manager)
        page_number = request.GET.get('page_number', 1)
        page_size = request.GET.get('page_size', 50)
        paginator = Paginator(task, page_size)
        serializer = self.serializer_class(paginator.page(page_number), many=True)
        return Response(serializer.data)
    
    def patch(self, request, id=None):
        try:
            manager = request.data.get('manager')
            status = request.data.get('status')
            task = get_object_or_404(Task, manager=manager, status=status)
            serializer = self.serializer_class(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except:
            return Response(({'message': 'details not found'}))
    
    
class ManagerCheckTaskView(APIView):
    serializer_class = TaskSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [Manager_required]
    
    
    def get(self, request, id=None):
        task = Task.objects.filter(manager=request.user.id)
        serializer = self.serializer_class(task, many=True)
        return Response(serializer.data)

    
class TaskStatusView(APIView):
    serializer_class = TaskSerializer
    authentication_classes = [authentication.TokenAuthentication]
    
    def get(self, request, id=None):
        task = Task.objects.filter(user__id=request.user.id)
        serializer = self.serializer_class(task, many=True)
        return Response(serializer.data)   
    
    
    

    
    