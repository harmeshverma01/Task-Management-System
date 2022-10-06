from rest_framework import serializers

from task.models import  Task

class TaskSerializer(serializers.ModelSerializer):
    # category = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = '__all__'
        
    # def get_category(self, obj):
    #     if obj.rating >= 1 and obj.rating < 4:
    #         return "Low"
    #     if obj.rating >= 4 and obj.rating < 7:
    #         return "High"
    #     if obj.rating >=7 and obj.rating < 10:
    #         return "Excellent"
     
        
class TaskCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['comment'] 
        
        
  
        

               