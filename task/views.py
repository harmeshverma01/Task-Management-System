from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.db.models import Avg

from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework import status

from user.utils import Manager_required, admin_required
from task.serializer import  TaskSerializer
from user.models import User
from .models import Task

# Create your views here.

class TaskView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = TaskSerializer
    permission_classes = [Manager_required]
    
    def post(self, request, id=None):
        user = request.data.get('user')
        if user == str(request.user.id): 
            return Response(({'message': "you can't assign task by own"}))
        is_admin = get_object_or_404(User, id=user)
        if is_admin.role=="admin":
            return Response(({'message': "you can't assign task to admin"}))
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
        params = self.request.query_params
        assign = Task.objects.all()
        admin = request.user.id
        if admin:
            task = assign.filter(manager=admin)
        manager = params.get('manager')
        if manager:
            task = assign.filter(manager=manager)
        status = params.get('status')    
        if status:
            task = assign.filter(status=status)
        user = params.get('user')    
        if user:
            task = assign.filter(user=user)
        page_number = request.GET.get('page_number', 1)
        page_size = request.GET.get('page_size', 50)
        paginator = Paginator(task, page_size)
        serializer = self.serializer_class(paginator.page(page_number), many=True)
        return Response(serializer.data)
    
    
class ManagerCheckTaskView(APIView):
    serializer_class = TaskSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [Manager_required]
    
    def get(self, request, id=None):
        params = self.request.query_params
        assign = Task.objects.all()
        manager = request.user.id
        if manager:
            task = assign.filter(user=manager)
        user = params.get('user')
        if user:
            task = assign.filter(manager=manager, user=user)
        status = params.get('status')
        if status:
            task = task.filter(status=status)
        page_number = request.GET.get('page_number', 1)
        page_size = request.GET.get('page_size', 50)
        paginator = Paginator(task, page_size)
        serializer = self.serializer_class(paginator.page(page_number), many=True)
        return Response(serializer.data)
    
    
class TaskStatusView(APIView):
    serializer_class = TaskSerializer
    authentication_classes = [authentication.TokenAuthentication]
    
    def get(self, request, id=None):
        params = self.request.query_params
        task = Task.objects.filter(user__id=request.user.id)
        manager = params.get('manager', None)
        if manager:
            task = task.filter(manager=manager)
        status = params.get('status', None)
        if status:
            task = task.filter(status=status)
        page_number = request.GET.get('page_number', 1)
        page_size = request.GET.get('page_size', 50)
        paginator = Paginator(task, page_size)
        serializer = self.serializer_class(paginator.page(page_number), many=True)
        return Response(serializer.data)   
    
    
class ManagertoManagerView(APIView):
    serializer_class = TaskSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [Manager_required]
    
    def get(self, request, id=None):
        task = Task.objects.filter(manager=request.user.id)
        serializer = self.serializer_class(task, many=True)
        return Response(serializer.data)
    
    
class TaskCompleteView(APIView):
    serializer_class = TaskSerializer
    authentication_classes = [authentication.TokenAuthentication]
    
    def get(self, request, id=None):
        if id:
            task = Task.objects.get(id=id)
            serializer = self.serializer_class(task)
            return Response(serializer.data)
        else:
            task = Task.objects.filter(user__id=request.user.id)
            serializer = self.serializer_class(task, many=True)
            return Response(serializer.data)
    
    def patch(self, request, id=None):
        try:
            assign = get_object_or_404(Task, id=id, user=request.user.id)
            serializer = self.serializer_class(assign, data=request.data, partial=True)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
            return Response(serializer.errors)
        except:
            return Response(({'details' : 'Task does not Found'}), status=status.HTTP_204_NO_CONTENT)
        
        
class TaskRatingView(APIView):
    serializer_class = TaskSerializer
    permission_classes = [Manager_required]
    authentication_classes = [authentication.TokenAuthentication]
    
    def get(self, request, id=None):
        rating = Task.objects.filter(manager=request.user.id)
        serializer = self.serializer_class(rating, many=True)
        return Response(serializer.data)
 
    def patch(self, request, id=None):
        rating = get_object_or_404(Task, id=id, manager=request.user.id)
        if rating:
            serializer = self.serializer_class(rating, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
            return Response(serializer.errors)
        else:
            return Response(({'messsage': "you don't have a access to give rating"}), status=status.HTTP_400_BAD_REQUEST)


class UserCheckTaskRatingView(APIView):
    serializer_class = TaskSerializer
    authentication_classes = [authentication.TokenAuthentication]
    
    def get(self, request, id=None):
        rating = Task.objects.filter(user=request.user.id)
        avg_rating = rating.aggregate(Avg('rating'))['rating__avg']
        count_rating = rating.count()
        task_count = rating.filter(user=request.user.id).count()
        serializer = self.serializer_class(rating, many=True)
        data = serializer.data
        context = {
            'avg_rating' : avg_rating,
            'count_rating' : count_rating,
            'task_count' : task_count,
            'data' : data
        }
        return Response(context, status=status.HTTP_200_OK)
     
    
class ManagerCheckTasKRatingView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = TaskSerializer
    permission_classes = [Manager_required]
    
    def get(self, request, id=None):
        rating = Task.objects.filter(manager=request.user.id)
        if rating:
            low = rating.filter(rating__range=['1', '4']).values()
            print(low, "low")
        if rating:
            high = rating.filter(rating__range=['4', '7']).values()
            print(high, "high")
        if rating:
            Excellent = rating.filter(rating__range=['7', '10']).values()
        values = {
            'Low' : low,
            'High' : high,
            'Excellent' : Excellent
        }
        serializer = self.serializer_class(values)
        avg_rating = rating.aggregate(Avg('rating'))['rating__avg']
        count_rating = rating.count()
        serializer = self.serializer_class(values, many=True)
        data = serializer.data
        context = {
            'avg_rating' : avg_rating,
            'count_rating' : count_rating,
            'data' : data
        }
        return Response(context, status=status.HTTP_200_OK)

    
    
    