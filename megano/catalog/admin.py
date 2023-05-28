from django.contrib import admin
from .models import CategoryIcon, Category
  
  
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