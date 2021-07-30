from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.lookups import Regex
#from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=250, unique=True)
    password = models.CharField(max_length=1000)
    otp = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

   
    

    def __str__(self):
        return self.email



class CreateMovie(models.Model):
    #user_id = models.CharField(max_length=20)
    movie_name = models.CharField(max_length=100)

    def __str__(self):
        return self.movie_name


class MovieReview(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(CreateMovie, on_delete=models.CASCADE)
    rating = models.CharField(max_length=100, null=True, blank=True)
    comment = models.CharField(max_length=1000)
    is_like = models.IntegerField(default=0)

    def __str__(self):
        return self.rating


class ResetPhoneOTP(models.Model):
    phone_regex = RegexValidator(regex = r'^\+?1?\d{9,14}$', message = "Phone number must be entered in the form of +919999999999.")
    phone = models.CharField(validators=[phone_regex], max_length=20, blank=True)
    otp = models.CharField(max_length=9, blank=True, null=True)
    count = models.IntegerField(default=0, help_text='Number of opt_sent')
    validated = models.BooleanField(default=False, help_text='if it is true, that mean user have validate opt correctly in seconds')

    def __str__(self):
        return str(self.phone) + ' is sent ' + str(self.otp)





