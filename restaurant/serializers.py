from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from restaurant import models as res_model

User = get_user_model()

# RegisterSerializer handles the registration of new users, including setting roles (owner or employee).
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'is_owner', 'is_employee']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Token.objects.create(user=user)
        print('#############################')
        print('Create New User')
        print('#############################')
        return user
    

# Serializer Restaurant model instances for API views.
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = res_model.Restaurant
        fields = '__all__'


# Serializer Category model instances for API views.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = res_model.Category
        fields = '__all__'


# Menue Item Serializer
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = res_model.MenuItem
        fields = '__all__'


class ModifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = res_model.Modifier
        fields = '__all__'