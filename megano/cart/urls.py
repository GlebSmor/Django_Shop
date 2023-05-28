from django.urls import path

from cart.views import BasketOfProductsView

app_name = 'cart'

urlpatterns = [
    path('api/basket/', BasketOfProductsView.as_view(), name='basket'),
    path('api/cart/', BasketOfProductsView.as_view(), name='cart'),
]