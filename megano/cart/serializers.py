from decimal import Decimal

from rest_framework import serializers

from products.models import Product


class BasketSerializer(serializers.ModelSerializer):
    """
    Сериализация корзины продуктов
    """
    count = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields = '__all__'

    def get_count(self, obj):
        return self.context.get(str(obj.pk)).get('count')

    def get_price(self, obj):
        return Decimal(self.context.get(str(obj.pk)).get('price'))
    
    def get_images(self, instance):
        images = []
        images_tmp = instance.images.all()
        for image in images_tmp:
            images.append({"src": f"/media{image.__str__()}", "alt": image.name})
        return images