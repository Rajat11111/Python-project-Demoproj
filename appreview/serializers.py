from django.contrib.auth import get_user_model
from rest_framework import serializers
from appreview.models import CreateMovie, CustomUser, MovieReview
from django.contrib.auth.models import User










# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email',"password")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['email'], validated_data['password'])

        return user


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateMovie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReview
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    movie_id =  MovieSerializer()
    class Meta:
        model = MovieReview
        fields = '__all__'





class PasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required = True)


