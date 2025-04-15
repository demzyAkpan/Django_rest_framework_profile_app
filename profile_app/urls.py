from django.urls import path
from views import UserProfileList, UserProfileDetail, Follow, FollowDelete

urlpatterns =[ 

   path('profiles/', UserProfileList.as_view(), name='user-profile-list'),#create a new profile
   path('profiles/<int:pk>/', UserProfileDetail.as_view(), name='user-profile-detail'),#get a specific profile
   path('profiles/<int:pk>/follow/', Follow.as_view(), name='follow-user'),#follow a user
   path('profiles/<int:pk>/unfollow/', FollowDelete.as_view(), name='unfollow-user'),#unfollow a user
   path('profiles/<int:pk>/followers/', UserProfileDetail.as_view(), name='user-followers'),#get followers of a user
   
]