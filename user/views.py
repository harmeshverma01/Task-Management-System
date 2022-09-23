from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from .serializer import LoginSerializer, UserSerializer
from .utils import admin_required
from .models import User
# Create your views here.

class Userview(APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, admin_required]
    authentication_classes = [authentication.TokenAuthentication]
    
    def get(self, request, id=None):
        user = User.objects.all()
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class Loginview(APIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        user = authenticate(email=request.data.get('email'),password=request.data.get('password'))
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({'token' : str(token[0])})
        return Response({'details' : 'User not Found'}, status=status.HTTP_204_NO_CONTENT)
    
    
class UserdetailsView(APIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    
    def get(self, request, id=None):
        user = User.objects.get(id=request.user.id)
        serializer = self.serializer_class(user)
        return Response(serializer.data)
    
    def patch(self, request, id=None):
        try:
            user = User.objects.get(id=request.user.id)
            serializer = self.serializer_class(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
            return Response(serializer.errors)
        except:
            return Response(({'message' : 'User does not found'}), status=status.HTTP_204_NO_CONTENT)
        
    def delete(self, request, id=None):
        user = User.objects.get(id=id)
        user.delete()
        return Response(({'message': 'user is deleted successfully'}), status=status.HTTP_204_NO_CONTENT)


class ManagerView(APIView):
    serializer_class = UserSerializer
    # permission_classes = [admin_required]
    
    def get(self, request, id=None):
        manager = User.objects.filter(role='manager')
        serializer = self.serializer_class(manager, many=True)
        return Response(serializer.data)
        