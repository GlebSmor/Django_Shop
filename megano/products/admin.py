from django.contrib import admin
from .models import (Product, ProductImage, Tag, Review, 
                     ProductSpecification, Sale)


@admin.register(Product)
class  ProductAdmin(admin.ModelAdmin):
    list_display = "pk", "title", "price", "category", "active"
    list_display_links = "pk", "title"
    ordering = "pk",
    
    
@admin.register(ProductImage)
class  ProductImageAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "product"
    list_display_links = "pk", "name"
    ordering = "pk",
    
    
@admin.register(Tag)
class  TagAdmin(admin.ModelAdmin):
    list_display = "pk", "name"
    list_display_links = "pk", "name"
    ordering = "pk",

    
    
@admin.register(Review)
class  ReviewAdmin(admin.ModelAdmin):
    list_display = "pk", "author", "product", "date"
    list_display_links = "pk",
    ordering = "pk",


@admin.register(ProductSpecification)
class  ProductSpecificationAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "value", "product"
    list_display_links = "pk", "name"
    ordering = "pk",


@admin.register(Sale)
class  SaleAdmin(admin.ModelAdmin):
    list_display = "pk", "title"
    list_display_links = "pk", 
    ordering = "pk",