from django.shortcuts import render, get_object_or_404
from .models import Profile, Follow
from .serializers import ProfileSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class UserProfileList(APIView):

    def get(self, request):
        query_profiles = Profile.objects.all()
        serializer = ProfileSerializer(query_profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserProfileDetail(APIView):
    """
    Retrieve a user's profile details, including followers and following counts.
    """
    def get(self, request, pk):
        query_profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializer(query_profile)

        data = serializer.data
        data['followers_count'] = query_profile.followers_count
        data['following_count'] = query_profile.following_count
        



        return Response(serializer.data, status=status.HTTP_200_OK)
            

class FollowUserView(APIView):
    def post(self, request, pk):
        try:
            user_to_follow = User.objects.get(pk=pk)
            if request.user == user_to_follow:
                return Response({"error": "you cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
            
            follow, created = Follow.objects.get_or_create(follower=request.user, following= user_to_follow)

            if created:
                return Response({"message":f'you are now following {user_to_follow}'})
            return Response({"message":"you are already following  this user."})
        
        except User.DoesNotExist:
            return Response({"error": "user not found"}, status=404)
        
class FollowDelete(APIView):
    def delete(self, request, pk):
        try:
            user_to_unfollow = User.objects.get(pk=pk)
            
            follow = Follow.objects.filter(follower=request.user, following=user_to_unfollow) #

            if follow.exists():
                follow.delete()
                return Response({"message":f'you have unfollowed {user_to_unfollow}'})
            return Response({"message":"you are not following this user."})
        
        except User.DoesNotExist:
            return Response({"error": "user not found"}, status=404)

