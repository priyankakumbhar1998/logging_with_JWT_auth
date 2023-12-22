from rest_framework.views import APIView
from .serializers import UserSerializers
from rest_framework import status
from rest_framework.response import Response
import logging

error_logger = logging.getLogger('error_logging')
success_logger = logging.getLogger('success_logger')

class UserAPI(APIView):
    def post(self, request):
        try:
            serializer = UserSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            success_logger.info(f"The User with username: {serializer.data.get('username')} created successfully")

        except Exception as e:
            error_logger.error(f"Error saving the user data {serializer.errors}")
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    