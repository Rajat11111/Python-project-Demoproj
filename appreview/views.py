from django.core.validators import EmailValidator
from django.db.models.query import QuerySet
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import PasswordSerializer, UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import Permission, User
from rest_framework.permissions import IsAuthenticated   
from .models import CreateMovie, MovieReview, ResetPhoneOTP
from .serializers import MovieSerializer
from .serializers import ReviewSerializer
from django.http import JsonResponse
from .serializers import ReviewListSerializer
import random
from .models import CustomUser










# def create_movie(request):
#     if request.method == 'POST':
#         create = CreateMovie.objects.all()
#         serializer = MovieSerializer(create, many=True)
#         return JsonResponse(serializer.data, safe=False)


class Movie_review(generics.GenericAPIView):
    #serializer_class = ReviewSerializer

    def post(self, request, *args, **kwargs):

        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()
        return Response({
        "user": ReviewSerializer(user, context=self.get_serializer_context()).data,
        })

class RatingList(generics.GenericAPIView):


    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        rate_list = MovieReview.objects.filter(rating__gte=3, is_like = 1)

        serializer = ReviewListSerializer(rate_list, many=True)
        return Response(serializer.data)


class LikesReview(generics.GenericAPIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        rate_list = MovieReview.objects.filter(rating__gte=3, is_like = 1)
        serializer =  ReviewListSerializer(rate_list, many=True)
        return Response(serializer.data)


class create_movie(generics.GenericAPIView):
    #serializer_class = MovieSerializer

    def post(self, request, *args, **kwargs):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": MovieSerializer(user, context=self.get_serializer_context()).data,
        })



class Movie_Delete(generics.GenericAPIView):
    serializer_class = ReviewSerializer
    def delete(self, request, pk):
        del_list =  MovieReview.objects.filter(movie_id=pk)
        if len(del_list) == 0:
            try:

                del_movi = CreateMovie.objects.get(id=pk)
                del_movi.delete()
                return Response({"messages": "deleted"}, status=status.HTTP_201_CREATED)
            except:
                return Response({"messages" : "This movie does not exists"})

        else:
            return Response({"messages": "movie has reviews"})

        # return Response(status=status.HTTP_204_NO_CONTENT)


class Random_otp(generics.GenericAPIView):
    def post(self, request):
        try:
            obj = CustomUser.objects.get(email = request.data['email'])
        except:
            obj = None

        if obj is None:
            return Response({"messages":"user not found"})
        else:
            obj.otp = 1234
            obj.save()
            return Response({"messages": "otp_generated"})


class Otp_verify(generics.GenericAPIView):
    def post(self, request):
        try:

            obj = CustomUser.objects.get(email = request.data['email'], otp = request.data['otp'])
            if obj.otp == 1234:
                obj.is_active = True
                obj.save()
                return Response({"messages" : "veryfied"})
        except:
            return Response({"messages":"otp is wrong"})
        # else:
        #     return Response({"messages" : "error"})
           
        






# class UserViewSet(generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = PasswordSerializer

#     def post(self, request):
#         phone = request.data.get('phone', False)
#         if phone:
#             old = ResetPhoneOTP.objects.filter(phone__iexact = phone)
#             if old.exists():
#                 old = old.last()
#                 validated = old.validated

#                 if validated:
#                     serializer = PasswordSerializer(data=request.data)
#                     if serializer.is_valid():
#                         User.set_password(serializer.data.get('new_password'))
#                         User.save()
#                         return Response({'status': 'password set'}, status=status.HTTP_200_ok)
#                     return Response({'status': 'password not2 set'})
#                 return Response({'status': 'password not3 set'})
#             return Response({'status': 'password not4 set'})


# class ResetPassword(generics.GenericAPIView):
#     Permission_classes = (IsAuthenticated,)
#     def post(self, request, *args, **kwargs):
#         phone_number = request.data.get('phone' )
        
#         if phone_number :
#             phone  = str(phone_number)
#             keygen = ResetPassword()
#             key = base64.b32encode(keygen.returnValue(phone).encode())
#             old = User.objects.filter(phone=phone)
#             if old.exists():
#                 ResetPhoneOTP.objects.create(
                    
#                     phone = phone,
#                     otp = key

#                     )
#                 return Response({
#                         'status' : True,
#                         'detail' : 'OTP sent successfully.'
#                         })
#             else:
#                 return Response({
#                     'status' : False,
#                     'detail' : 'Phone Number DoesNotExist'
#                 })
#         else:
#             return Response({
#                 'status' : False,
#                 'detail' : 'Phone Number is not given in body.'
#             })

# class ValidateResetOTP(generics.GenericAPIView):
#     permission_classes = (IsAuthenticated,)
#     def post(self, request, *args, **kwargs):
#         phone = request.data.get('phone' , False)
#         otp_sent = request.data.get('otp', False)

#         if phone and otp_sent:
#             old = ResetPhoneOTP.objects.filter(phone__iexact = phone)
#             if old.exists():
#                 old = old.last()
#                 otp = old.otp
#                 #old = Customer.objects.filter(otp)
#                 if str(otp_sent) == str(otp):
#                     old.validated = True
#                     old.save()
#                     return Response({
#                         'status' : True,
#                         'detail' : 'OTP mactched. Please proceed for Reset Password.'
#                         })
#                 else: 
#                     return Response({
#                         'status' : False,
#                         'detail' : 'OTP incorrect.'
#                         })
#             else:
#                 return Response({
#                     'status' : False,
#                     'detail' : 'First proceed via sending otp request.'
#                     })
#         else:
#             return Response({
#                 'status' : False,
#                 'detail' : 'Please provide both phone and otp for validations'
#                 })




        
       
        
        
       

    
    







class movies_list_view(generics.GenericAPIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        list = CreateMovie.objects.all()
        serializer = MovieSerializer(list, many=True)
        return Response(serializer.data)










# Register API
class RegisterAPI(generics.GenericAPIView):
    #serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer =  RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        print(request.data)
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)