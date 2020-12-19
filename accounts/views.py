from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from accounts.serializers import UserSerializer,AuthTokenSerializer

class CreateUserView(generics.CreateAPIView):
    """create a new user  in system"""
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrive and return authentication user"""
        return self.request.user
    
    
# from rest_framework.views import APIView
# from rest_framework.views import Response
# from rest_framework import status
# from rest_framework import viewsets

# from accounts.models import Custom_User

# from rest_framework.permissions import IsAdminUser
# from rest_framework.mixins import CreateModelMixin
# from rest_framework import filters
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from rest_framework.authtoken.views import ObtainAuthToken

# from django.http import HttpResponse, JsonResponse
# from rest_framework.decorators import api_view
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.contrib.auth import get_user_model
# Create your views here.


# class CreateUserView(viewsets.ModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('mobile_no','username',)

# class LoginViewset(viewsets.ModelViewSet):
       
#     serializer_class = AuthTokenSerializer
#     def create(self, request):

#         return ObtainAuthToken().post(request)


        

# @api_view(["POST"])
# def user_login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")

#     user = authenticate(username = username,password=password)
#     if not user:
#         return Response({"error":"Login Failed"},status=HTTP_401_UNAUTHORIZED)
#     else :
#         return Response({"success":"Login Successfully"})    
# # class
# @csrf_exempt
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Custom_User.objects.all()
#         serializer = NewSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = NewSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Custom_User.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = NewSerializer(snippet)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = NewSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)

# class all_user_api(viewsets.ModelViewSet):
#     serializer_class = serializers.UserSerializer
#     queryset = Custom_User.objects.all()

# class all_user_api(APIView):
#     permission_classes = [IsAdminUser]

#     def get(self, format=None):
#         users = Custom_User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=ValueError):
#             serializer.create(validated_data=request.data)
#             return Response(
#                 serializer.data,
#                 status=status.HTTP_201_CREATED
#             )
#         return Response(
#             {
#                 "error": True,
#                 "error_msg": serializer.error_messages,
#             },
#             status=status.HTTP_400_BAD_REQUEST
#         )

# class all_user_api(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
