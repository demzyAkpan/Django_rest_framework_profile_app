from django.urls import path
from .views import UserProfileList, UserProfileDetail, FollowUserView, FollowDelete

urlpatterns = [
    path('profiles/', UserProfileList.as_view(), name='user-profile-list'),  # List all profiles
    path('profiles/<int:pk>/', UserProfileDetail.as_view(), name='user-profile-detail'),  # Get a specific profile
    path('profiles/follow/<int:pk>/', FollowUserView.as_view(), name='follow-user'),  # Follow a user
    path('profiles/unfollow/<int:pk>/', FollowDelete.as_view(), name='unfollow-user'),  # Unfollow a user
   #  path('profiles/<int:pk>/followers/', UserFollowersView.as_view(), name='user-followers'),  # Get followers of a user
]
