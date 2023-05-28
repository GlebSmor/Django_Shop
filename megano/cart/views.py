from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.cart import Cart
from cart.serializers import BasketSerializer
from products.models import Product


def get_products_in_cart(cart):
    """
    Получение продуктов из корзины и их сериализация
    :param cart: корзина продуктов
    :return: сериализованные данные
    """
    products_in_cart = [product for product in cart.cart.keys()]
    products = Product.objects.filter(pk__in=products_in_cart)
    serializer = BasketSerializer(products, many=True, context=cart.cart)
    return serializer


class BasketOfProductsView(APIView):
    """
    Представление для получения и удаления продуктов из корзины, добавления продуктов в корзину
    """

    def get(self, *args, **kwargs):
        cart = Cart(self.request)
        serializer = get_products_in_cart(cart)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        cart = Cart(self.request)
        product = get_object_or_404(Product, id=self.request.data.get('id'))
        cart.add(product=product, count=self.request.data.get('count'))
        serializer = get_products_in_cart(cart)
        return Response(serializer.data)

    def delete(self, *args, **kwargs):
        print(self.request.data, '\n')
        cart = Cart(self.request)
        product = get_object_or_404(Product, id=self.request.data.get('id'))
        count = self.request.data.get('count', False)
        cart.remove(product, count=count)
        serializer = get_products_in_cart(cart)
        return Response(serializer.data)