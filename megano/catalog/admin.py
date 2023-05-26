from django.contrib import admin
from .models import *


@admin.register(Product)
class  ProductAdmin(admin.ModelAdmin):
    list_display = "pk", "title", "date"
    list_display_links = "pk", "title"
    ordering = "pk",
    
    
@admin.register(ProductImage)
class  ProductImageAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "product", "verbose_product"
    list_display_links = "pk", "name"
    ordering = "pk",
    
    def verbose_product(self, obj: ProductImage):
        return obj.product.title
    
    
@admin.register(Tag)
class  TagAdmin(admin.ModelAdmin):
    list_display = "pk", "name"
    list_display_links = "pk", "name"
    ordering = "pk",

    
    
@admin.register(Review)
class  ReviewAdmin(admin.ModelAdmin):
    list_display = "pk", "author", "date"
    list_display_links = "pk",
    ordering = "pk",


@admin.register(ProductSpecification)
class  ProductSpecificationAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "value", "get_product_name"
    list_display_links = "pk", "name"
    ordering = "pk",
    
    def get_product_name(self, obj: ProductSpecification):
        return obj.product.title
    
@admin.register(Category)
class  CategoryAdmin(admin.ModelAdmin):
    list_display = "pk", "title"
    list_display_links = "pk", "title"
    ordering = "pk",
    
    
@admin.register(CategoryIcon)
class  CategoryIconAdmin(admin.ModelAdmin):
    list_display = "pk", "alt"
    list_display_links = "pk", 
    ordering = "pk",
    
    
@admin.register(Sale)
class  SaleAdmin(admin.ModelAdmin):
    list_display = "pk", "title"
    list_display_links = "pk", 
    ordering = "pk",