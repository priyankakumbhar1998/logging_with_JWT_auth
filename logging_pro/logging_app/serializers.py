from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"


    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    
