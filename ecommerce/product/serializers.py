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




class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id','photo', 'product')

class AtributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atribute
        fields = ('id','title', 'value','product',)
        # ('title','value','products')

#product serializers
class ProducteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    atributes = AtributeSerializer(many=True)
    photos = PhotoSerializer(many=True, )

    class Meta:
        model = Producte
        fields =('id','title','description','price','category','user','created_date','atributes','photos') 
        
    def create(self, validated_data):
        atributes_data = validated_data.pop('atributes', [])
        photos_data = validated_data.pop('photos', [])

        product = Producte.objects.create(**validated_data)

        for atribute_data in atributes_data:
            Atribute.objects.create(product=product, **atribute_data)

        for photo_data in photos_data:
            Photo.objects.create(product=product, **photo_data)

        return product
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.category = validated_data.get('category', instance.category)

        # Update nested serializers (attributes and photos)
        atributes_data = validated_data.get('atributes')
        if atributes_data:
            instance.atributes.all().delete()
            for atribute_data in atributes_data:
                instance.atributes.create(**atribute_data)
        
        photos_data = validated_data.get('photos')
        if photos_data:
            instance.photos.all().delete()
            for photo_data in photos_data:
                instance.photos.create(**photo_data)

        instance.save()
        return instance

        
class CategotyProducts(serializers.ModelSerializer):
    class Meta:
        model = Producte
        fields = ('id','title','description','price','category','created_date')
        



class CategorySerializer(serializers.ModelSerializer):
    # products = CategotyProducts(many=True)
    class Meta:
        model = Category
        fields ="__all__" 
        # ('title','description')


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ("id","order","product","quantity","status","get_total_item_price")       



class OrderSerializer(serializers.ModelSerializer):
    user =  serializers.HiddenField(default=serializers.CurrentUserDefault())
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ("id","ordered_date","shipping_address","payment","items","user","get_total")       
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        
        for order_item_data in items_data:
            OrderItem.objects.create(order=order, **order_item_data)
        
        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', [])
        instance.customer = validated_data.get('user', instance.user)
        
        # Update or create order items
        instance.items.all().delete()
        for item_data in items_data:
            OrderItem.objects.create(order=instance, **item_data)

        instance.save()
        return instance
