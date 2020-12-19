from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):

  def create_user(self,email,password=None,**extra_fields):
    """create and save a new user"""
    if not email:
      raise ValueError('Users must have an email address')
    user = self.model(email=email,**extra_fields)
    user.set_password(password)
    user.save(using=self._db)

    return user

  def create_superuser(self,email,password):
    """craete and save superuser"""
    user = self.create_user(email,password)
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)
  
    return user

class User(AbstractBaseUser,PermissionsMixin):
  """custom user model that support using email """
  email = models.EmailField(max_length=255,unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects = UserManager()

  USERNAME_FIELD = 'email'


# class Custom_User(AbstractUser):
#     SUPERADMIN = 1
#     ADMIN = 2
#     MEMBER = 3
#     ROLE_CHOICES = (
#       (ADMIN,'Admin'),
#       (SUPERADMIN,'Super Admin'),
#       (MEMBER,'Member'))
#     user_role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=ADMIN,blank=True)
#     uid = models.CharField(max_length=264,blank=True)
#     mobile_no = models.CharField(max_length=264,blank=True)
#     panid = models.CharField(max_length=264,blank=True)
#     user_varified = models.CharField(max_length=264,blank=True)
#     update_on = models.DateTimeField(auto_now=True)
   