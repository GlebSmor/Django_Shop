from django.urls import path
from .views import (TagsList, ProductDetail, LimitedList, 
                    PopularList, SalesList, CreateReview)

urlpatterns = [
    path('api/product/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('api/product/<int:pk>/reviews/', CreateReview.as_view()),
    path('api/tags/', TagsList.as_view(), name='tags_list'),
    path('api/products/popular/', PopularList.as_view(), name='popular'),
    path('api/products/limited/', LimitedList.as_view(), name='limited'),
    path('api/sales/', SalesList.as_view(), name='sales'),
]