from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework import status

from task.serializer import TaskSerializer
from user.utils import Manager_required
from .models import Task

# Create your views here.

class TaskView(APIView):
    serializer_class = TaskSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [Manager_required]
    
    def post(self, request):
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
                

class CheckCompletedtaskView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [Manager_required]
    serializer_class = TaskSerializer
    
    def get(self, request, id=None):
        task = Task.objects.all()
        completed = request.GET.get('completed', None)
        if completed is not None:
            task = task.filter(completed=completed)
        serializer = self.serializer_class(task, many=True)
        return Response(serializer.data)
    
    
class TaskStatusView(APIView):
    serializer_class = TaskSerializer
    authentication_classes = [authentication.TokenAuthentication]
    
    def get(self, request, id=None):
        task = Task.objects.filter(user__id=request.user.id)
        serializer = self.serializer_class(task, many=True)
        return Response(serializer.data)    

    

                