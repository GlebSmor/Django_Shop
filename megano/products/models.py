from django.db import models
from catalog.models import Category


def product_image_directory_path(instanse: "ProductImage", filename):
    return f"products/images/{instanse.product.pk}/{filename}"


class Product(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    description = models.CharField(max_length=256, null=False, blank=True)
    fullDescription = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, null=False)
    count = models.IntegerField(default=0, null=False)
    date = models.DateTimeField(auto_now_add=True, null=False)
    freeDelivery = models.BooleanField(default=True)
    limited_edition = models.BooleanField(default=False)
    rating = models.DecimalField(default=0, max_digits=3, decimal_places=2, null=False)
    active = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    class Meta:
        verbose_name="Product"
        verbose_name_plural="Products"
        ordering = ["pk",]
        
    def __str__(self):
        return self.title


class ProductSpecification(models.Model):

    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="specifications")
    name = models.CharField(max_length=256, default="")                    
    value = models.CharField(max_length=256, default="")

    class Meta:
        verbose_name = "Product specification"
        verbose_name_plural = "Product specifications"
    
    
class ProductImage(models.Model):
    name = models.CharField(max_length=128, null=False, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", verbose_name="product")
    image = models.FileField(upload_to=product_image_directory_path)
    
    class Meta:
        verbose_name="Product image"
        verbose_name_plural="Product images"
        ordering = ["pk",]
        
    def src(self):
        return self.image

    def __str__(self):
        return f"/{self.image}"

    
class Tag(models.Model):
    name = models.CharField(max_length=128, null=False, blank=True)
    product = models.ManyToManyField(Product, related_name="tags", verbose_name="product")
    
    class Meta:
        verbose_name="Tag"
        verbose_name_plural="Tags"
        ordering = ["pk",]
        
    def __str__(self):
        return self.name
    

class Review(models.Model):
    author = models.CharField(max_length=128)
    email = models.EmailField(max_length=256)
    text = models.TextField()
    rate = models.PositiveSmallIntegerField(blank=False, default=5)
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="reviews", verbose_name="product")
    
    class Meta:
        verbose_name="Review"
        verbose_name_plural="Reviews"
        ordering = ["pk",]
        
    def __str__(self):
        return f"{self.author}: {self.product.title}"
    
    
class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')
    salePrice = models.DecimalField(max_digits=10, db_index=True, decimal_places=2, default=0)
    dateFrom = models.DateField(default='')
    dateTo = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'
    
    
    def price(self):
        """
        Получение первоначальной цены продукта
        :return: цена
        """
        return self.product.price

    def title(self):
        """
        Получение названия продукта
        :return: название продукта
        """
        return self.product.title

    def href(self):
        """
        Получение ссылки на детальную страницу продукта
        :return: ссылка
        """
        return f'/product/{self.product.pk}'

    def __str__(self):
        return self.product.title
