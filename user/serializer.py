from rest_framework import serializers
from .models import Assign, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'role']
       
        
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
    
        
class AssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assign
        fields = '__all__'       