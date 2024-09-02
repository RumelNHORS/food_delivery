from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import RegisterSerializer

User = get_user_model()


# RegisterUserView handles the registration of new users and returns an authentication token.
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

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
            'is_owner': user.is_owner,
            'is_employee': user.is_employee,
        })

