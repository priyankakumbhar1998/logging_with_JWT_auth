from .serializers import StudentSerializer
from rest_framework.views import APIView
from .models import Student
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
import logging
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


error_logger = logging.getLogger('error_logger')
success_logger = logging.getLogger('success_logger')


class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)
            success_logger.info(f"Student fetched successfully")
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            error_logger.error(f"There is an error fetching the student")
            return Response(data={'detail': 'There is an error fetching the student'}, status=status.HTTP_400_BAD_REQUEST)

    
    def post(self , request):
        try:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                success_logger.info('Student created successfully')
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as E:
            error_logger.info(f'There is an error fetching student {serializer.errors}')
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class StudentDetailsAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request, pk=None):
        try:
            student= get_object_or_404(Student, pk=pk)
            serializer = StudentSerializer(student)
            success_logger.info(f'student details retrieved: {serializer.data}')
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            error_logger.error(f"There is an error fetching the student")
            return Response(data=serializer.error, status=status.HTTP_400_BAD_REQUEST)


    def delete (self, request, pk=None):
        try:
            student = get_object_or_404(Student, pk=pk)
            student.delete()
            success_logger.info(f"Student deleted successfully: {pk}")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            error_logger.error(f"Failed to delete student")
            return Response(data={'detail': 'Error deleting student'}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        try:
            student = get_object_or_404(Student, pk=pk)
            serializer = StudentSerializer(student, data=request.data,)
            if serializer.is_valid():
                instance = serializer.save()
                success_logger.info(f'Student updated successfully: {instance}')
                return Response(data=serializer.data , status=status.HTTP_200_OK)
        except Exception as e:
            error_logger.info(f'Failed to update student data {serializer.errors}')
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        try:
            student = get_object_or_404(Student, pk=pk)
            serializer = StudentSerializer(data=request.data, instance=student, partial=True)
            if serializer.is_valid():
                instance = serializer.save()
                success_logger.info(f'Student data partially updated successfully {instance}')
                return Response(data=serializer.data,  status=status.HTTP_200_OK)
        except Exception as e:
            error_logger.info(f'There is an error fetching student {serializer.errors}')
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            


    

        

    

    

    



