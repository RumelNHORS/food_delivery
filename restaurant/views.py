from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from restaurant import serializers as res_serializer
from restaurant import models as res_models
from restaurant import permissions as res_permissions

User = get_user_model()


# RegisterUserView handles the registration of new users and returns an authentication token.
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = res_serializer.RegisterSerializer

    def create(self, request, *args, **kwargs):
        # Manually handle the user creation
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate the token
        token, created = Token.objects.get_or_create(user=user)
        # Return the response with the token and user data
        return Response({'token': token.key, 'user': serializer.data})


# CustomAuthToken handles user authentication and returns a token along with user details.
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'mail': user.email,
            'is_owner': user.is_owner,
            'is_employee': user.is_employee,
        })


# List and create operations for Restaurant instances, restricted to owners and employees.
class RestaurantListCreateView(generics.ListCreateAPIView):
    queryset = res_models.Restaurant.objects.all()
    serializer_class = res_serializer.RestaurantSerializer
    permission_classes = [IsAuthenticated, res_permissions.IsOwnerOrEmployee]


# Retrieve, Update, and Delete operations for Restaurant instances, restricted to owners and employees.
class RestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = res_models.Restaurant.objects.all()
    serializer_class = res_serializer.RestaurantSerializer
    permission_classes = [IsAuthenticated, res_permissions.IsOwnerOrEmployee]



# List and create operations for Category instances, restricted to owners and employees.
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = res_models.Category.objects.all()
    serializer_class = res_serializer.CategorySerializer
    permission_classes = [IsAuthenticated, res_permissions.IsOwnerOrEmployee]

# Retrieve, update, and delete operations for Category instances, restricted to owners and employees.
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = res_models.Category.objects.all()
    serializer_class = res_serializer.CategorySerializer
    permission_classes = [IsAuthenticated, res_permissions.IsOwnerOrEmployee]


# View For List and Create the Menue Item
class MenuItemListCreateView(generics.ListCreateAPIView):
    queryset = res_models.MenuItem.objects.all()
    serializer_class = res_serializer.MenuItemSerializer
    permission_classes = [IsAuthenticated, res_permissions.IsOwnerOrEmployee]


# View for Update and Delete the MenueItem
class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = res_models.MenuItem.objects.all()
    serializer_class = res_serializer.MenuItemSerializer
    permission_classes = [IsAuthenticated, res_permissions.IsOwnerOrEmployee]