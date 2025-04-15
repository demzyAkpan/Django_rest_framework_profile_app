from django.shortcuts import render, get_object_or_404
from .models import Profile
from .serializers import ProfileSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class UserProileList(APIView):

    def get(self, request):
        query_profiles = Profile.objects.all()
        serializer = ProfileSerializer(query_profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserProfileDetail(APIView):
    def get(self, request, pk):
        query_profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializer(query_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
            

class Follow
