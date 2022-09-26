from rest_framework import serializers

from task.models import CreateUser, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
        
class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateUser
        fields = '__all__'
                