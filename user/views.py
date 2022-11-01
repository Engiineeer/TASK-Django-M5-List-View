from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import UserLoginSerializer
from rest_framework.views import APIView




class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)
