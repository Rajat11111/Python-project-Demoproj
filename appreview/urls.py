from .views import LikesReview, Movie_review, RatingList, RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI
from .views import movies_list_view
from .views import create_movie
from .views import Movie_Delete
from .views import Random_otp
from .views import Otp_verify





urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('movielist/',movies_list_view.as_view(), name='movies_list_view'),
    path('createmovie/', create_movie.as_view(), name='create'),
    path('reviewmovie/', Movie_review.as_view(), name='review'),
    path('ratelist/', RatingList.as_view(), name='ratings'),
    path('likesreview/', LikesReview.as_view(), name='like'),
    path('deletemovie/<int:pk>/',Movie_Delete.as_view(), name='dele'),
    path('otp_generate/',Random_otp.as_view(), name='generate'),
    path('verify/', Otp_verify.as_view(), name='verified'),
    
   
   
  
]

