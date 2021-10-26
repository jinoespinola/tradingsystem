from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tradingsystem.models import Stock,Order

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = ['url', 'name', 'price']
        lookup_field = 'name'


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        foo = Order.objects.create(
            user=self.context['request'].user,
            stocks=self.context['stock'],
            **validated_data
        )
        return foo
    class Meta:
        model = Order
        fields = ['url', 'user', 'stocks', 'qty']