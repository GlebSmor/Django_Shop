from django.urls import path
from .views import Catalog, BannersList, CategoriesList

urlpatterns = [
    path('api/catalog/', Catalog.as_view(), name='products_list'),
    path('api/banners/', BannersList.as_view(), name='banners'),
    path('api/categories/', CategoriesList.as_view(), name='categories'),
]