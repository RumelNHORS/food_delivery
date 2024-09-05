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
    

# Serializer for Restaurant model
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = res_model.Restaurant
        fields = '__all__'


# Serializer for Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = res_model.Category
        fields = '__all__'


# Menue Item Serializer
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = res_model.MenuItem
        fields = '__all__'


# Modifier Model Serializer
class ModifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = res_model.Modifier
        fields = '__all__'


# Serializer for OrderItem model
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = res_model.OrderItem
        fields = ['id', 'menu_item', 'quantity', 'price']

# Serializer for Order model
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = res_model.Order
        fields = ['id', 'customer', 'restaurant', 'created_at', 'payment_method', 'total_amount', 'items']
        read_only_fields = ['id', 'customer', 'created_at', 'total_amount']

    # Custom create method to handle the creation of order and associated order items.
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = res_model.Order.objects.create(**validated_data)
        # Initialize total amount for the order.
        total_amount = 0
        # Loop through each item in the order items data.
        for item_data in items_data:
            menu_item = item_data['menu_item']
            item_price = menu_item.price * item_data['quantity']
            res_model.OrderItem.objects.create(order=order, price=item_price, **item_data)
            total_amount += item_price

        order.total_amount = total_amount
        order.save()

        return order
