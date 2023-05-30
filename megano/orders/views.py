from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status
from cart.cart import Cart
from .models import Order, CountProductinOrder
from orders.serializers import OrderSerializer
from users.models import Profile
from products.models import Product


class Orders(APIView):
    def post(self, request: Request, *args, **kwargs):
        
        products_in_order = [(obj["id"], obj["count"], obj["price"]) for obj in request.data]
        products = Product.objects.filter(id__in=[obj[0] for obj in products_in_order])
        order = Order.objects.create(
            user=request.user.profile,
            totalCost=Cart(request).total_price(),
        ) 
        data = {
            "orderId": order.pk,
        }
        order.products.set(products)
        order.save()
        return Response(data)
    
    def get(self, request: Request):
        data = Order.objects.all()
        serialized = OrderSerializer(data, many=True)
        return Response(serialized.data)

    
class OrderDetail(APIView):
    def get(self, request: Request, pk):
        data = Order.objects.get(pk=pk)
        serialized = OrderSerializer(data)
        cart = Cart(request).cart
        data = serialized.data
        
        try:
            products_in_order = data['products']
            query = CountProductinOrder.objects.filter(order_id=pk)
            prods = {obj.product.pk: obj.count for obj in query}
            for prod in products_in_order:
                    prod['count'] = prods[prod['id']]
        except:
            products_in_order = data['products']
            for prod in products_in_order:
                prod['count'] = cart[str(prod['id'])]['count']


        return Response(data)
    
    def post(self, request: Request, pk):

        order = Order.objects.get(pk=pk)
        data = request.data
        order.fullName = data['fullName']
        order.phone = data['phone']
        order.email = data['email']
        order.deliveryType = data['deliveryType']
        order.city = data['city']
        order.address = data['address']
        order.paymentType = data['paymentType']
        order.status = 'Ожидает оплаты'
        if data['deliveryType'] == 'express':
            order.totalCost += 500
        else:
            if order.totalCost < 2000:
                order.totalCost += 200

        for product in data['products']:
            CountProductinOrder.objects.get_or_create(
                order_id=order.pk,
                product_id=product['id'],
                count=product['count']
            )
                
        order.save()
        Cart(request).clear()
        return Response(request.data, status=status.HTTP_201_CREATED)
    
    
class PaymentView(APIView):
    
    def post(self, request: Request, pk):
        order = Order.objects.get(pk=pk)
        print(order.paymentType)
        print(request.data)
        order.status = 'Оплачен'
        order.save()
        return Response(request.data, status=status.HTTP_200_OK)
    
