from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer



class UserAPIList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserAPIView(APIView):
    def get(self, request):
        query = User.objects.all()
        return Response({'users': UserSerializer(query, many=True).data})

    def post(self, request):
        serializer_for_user = UserSerializer(data=request.data)
        serializer_for_user.is_valid(raise_exception=True)
        serializer_for_user.save()

        return Response({'new_user': serializer_for_user.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'Error': 'Method PUT not allowed'})

        try:
            user_id = User.objects.get(pk=pk)
        except:
            return Response({'Error': 'Object does not exists'})

        serializer_for_user = UserSerializer(data=request.data, instance=user_id)
        serializer_for_user.is_valid(raise_exception=True)
        serializer_for_user.save()

        return Response({'update_user': serializer_for_user.data})


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'Error': 'Method DELETE not allowed'})

        try:
            user_id = User.objects.get(pk=pk)
            user_id.delete()
        except:
            return Response({'Error': 'Object does not delete'})

        return Response({'delete_user': f'user with id {pk} was deleted'})