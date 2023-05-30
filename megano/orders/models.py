from django.db import models
from django.db import models
from products.models import Product
from users.models import Profile


class Order(models.Model):
    """
    Модель заказа
    """
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    user = models.ForeignKey(Profile, on_delete=models.PROTECT, verbose_name='пользователь', related_name='orders')
    deliveryType = models.CharField(max_length=128, default='', verbose_name='тип доставки')
    paymentType = models.CharField(max_length=128, default='', verbose_name='тип оплаты')
    totalCost = models.DecimalField(max_digits=10, default=0, decimal_places=2, verbose_name='сумма заказа')
    status = models.CharField(max_length=128, default='', verbose_name='статус')
    city = models.CharField(max_length=256, default='', verbose_name='город')
    address = models.CharField(max_length=256, default='', verbose_name='адрес')
    products = models.ManyToManyField(Product, related_name='orders', verbose_name='продуты')
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def email(self):
        return self.user.email

    def fullName(self):
        return self.user.fullName

    def phone(self):
        return self.user.phone

    def orderId(self):
        return f'{self.pk}'

    def __str__(self):
        return f'{self.pk}'


class CountProductinOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    count = models.PositiveIntegerField()