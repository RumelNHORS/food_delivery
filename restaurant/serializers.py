from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# RegisterSerializer handles the registration of new users, including setting roles (owner or employee).
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'is_owner', 'is_employee']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
