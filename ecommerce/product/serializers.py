from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Producte,Atribute,Category,Photo,Order,OrderItem


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


#product serializers
class ProducteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Producte
        fields =('title','description','price','category','user', 'photo') 
        # ('title','description','content','category')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ="__all__" 
        # ('title','description')

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('photo', 'product')

class AtributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atribute
        fields = ('product','title', 'value',)
        # ('title','value','products')

class OrderItemSerializer(serializers.ModelSerializer):
    user =  serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = OrderItem
        fields = "__all__"       

class OrderSerializer(serializers.ModelSerializer):
    user =  serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Order
        fields = "__all__"       



