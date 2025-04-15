from django.urls import path
from .views import UserProfileList, UserProfileDetail, FollowUserView, FollowDelete


urlpatterns =[ 

   path('profiles/', UserProfileList.as_view(), name='user-profile-list'),#create a new profile
   path('profiles/<int:pk>/', UserProfileDetail.as_view(), name='user-profile-detail'),#get a specific profile
   path('profiles/follow/<int:pk>/', FollowUserView.as_view(), name='follow-user'),#follow a user
   path('profiles/unfollow/<int:pk>/', FollowDelete.as_view(), name='unfollow-user'),#unfollow a user
   path('profiles/<int:pk>/followers/', UserProfileDetail.as_view(), name='user-followers'),#get followers of a user

]