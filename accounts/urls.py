from django.urls import path

from accounts.views import *

app_name='accounts'

urlpatterns = [
    path('create/',CreateUserView.as_view(),name='create'),
    path('token/',CreateTokenView.as_view(),name='token'),
    path('me/',ManageUserView.as_view(),name='me'),
]


# from django.contrib import admin
# from django.urls import path
# from rest_framework.viewsets import GenericViewSet
# from rest_framework.mixins import CreateModelMixin

# from django.conf.urls import include
# from rest_framework.routers import DefaultRouter

# from . import views

# app_name = 'accounts'

# router = DefaultRouter()
# router.register('createuser',views.CreateUserView)
# router.register('login',views.LoginViewset,base_name='login')

# urlpatterns = [
# path('',include(router.urls)),
# # path('user_login',views.user_login),
# # path('data_api',views.all_user_api.as_view(),name='data_api'),

# # path('snippets/', views.snippet_list),

# # path('snippets/<int:pk>/', views.snippet_detail),

# ]