from django.urls import path
from .views import (ProductsList, TagsList, ProductDetail, 
                    BannersList, CategoriesList, LimitedList,
                    PopularList, SalesList)

urlpatterns = [
    path('api/catalog/', ProductsList.as_view(), name='products_list'),
    path('api/product/<int:pk>/', ProductDetail.as_view()),
    path('api/tags/', TagsList.as_view(), name='tags_list'),
    path('api/banners/', BannersList.as_view(), name='banners'),
    path('api/products/popular/', PopularList.as_view(), name='popular'),
    path('api/products/limited/', LimitedList.as_view(), name='limited'),
    path('api/categories/', CategoriesList.as_view(), name='categories'),
    path('api/sales/', SalesList.as_view(), name='sales'),
]