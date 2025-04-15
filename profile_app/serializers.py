from rest_framework import serializers
from .models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'date_joined', 'followers_count', 'following_count']

class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'username', 'followers_count', 'following_count']
        

    def get_followers_count(self, obj):
        return obj.followers.count()
    
    def get_following_count(self, obj):
        return obj.following.count()

class UserProfileDetail(APIView):
    """
    Retrieve a user's profile details, including followers and following counts.
    """
    def get(self, request, pk):
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProfileSerializer(profile)
        return Response(serializer.data)