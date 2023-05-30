import datetime

from rest_framework import serializers
from orders.models import Order
from products.models import Product
from products.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    """
    Сериализация заказа
    """
    products = ProductSerializer(many=True,required=True)
    fullName = serializers.StringRelatedField()
    email = serializers.StringRelatedField()
    phone = serializers.StringRelatedField()
    createdAt = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_createdAt(self, instance):
        date = instance.createdAt + datetime.timedelta(hours=3)
        return datetime.datetime.strftime(date, '%d.%m.%Y %H:%M')