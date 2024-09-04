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


# View to list all Restaurants, restricted to all users.
class RestaurantListView(generics.ListAPIView):
    queryset = res_models.Restaurant.objects.all()
    serializer_class = res_serializer.RestaurantSerializer


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


# View to list all Categories, restricted to all users.
class CategoryListView(generics.ListAPIView):
    queryset = res_models.Category.objects.all()
    serializer_class = res_serializer.CategorySerializer


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


# View to list all MenuItems, restricted to all users.
class MenuItemListView(generics.ListAPIView):
    queryset = res_models.MenuItem.objects.all()
    serializer_class = res_serializer.MenuItemSerializer


# Views for Create and List of the Modifire
class ModifierListCreateView(generics.ListCreateAPIView):
    queryset = res_models.Modifier.objects.all()
    serializer_class = res_serializer.ModifierSerializer
    permission_classes = [IsAuthenticated, res_permissions.IsOwnerOrEmployee]

# Views for Update and Delete the modifire
class ModifierDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = res_models.Modifier.objects.all()
    serializer_class = res_serializer.ModifierSerializer
    permission_classes = [IsAuthenticated, res_permissions.IsOwnerOrEmployee]


# Create the view to handle the order creation.
class OrderCreateView(generics.CreateAPIView):
    queryset = res_models.Order.objects.all()
    serializer_class = res_serializer.OrderSerializer
    permission_classes = [IsAuthenticated] # If you thik unathenticated user can be order, then remove or Comment this line

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
