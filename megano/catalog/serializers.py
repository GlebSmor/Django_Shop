from rest_framework import serializers
from .models import Category, CategoryIcon


class CategoryIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryIcon
        fields = "id", "src", "alt"


class SubCategorySerializer(serializers.ModelSerializer):
    image = CategoryIconSerializer(many=False, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"
        
        
class CategorySerializer(serializers.ModelSerializer):
    image = CategoryIconSerializer(many=False, required=False)
    subcategories = SubCategorySerializer(many=True, required=False)
    
    # def get_image(self, instance):
        
    #     return {"src": f"/media/{instance.image.href}"}
    
    class Meta:
        model = Category
        fields = "__all__"
        
        