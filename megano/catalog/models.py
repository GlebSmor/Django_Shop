from django.db import models


def category_image_directory_path(instance: "CategoryIcon", filename):

    if instance.category.parent:
        return f"catalog/icons/{instance.category.parent}/{instance.category}/{filename}"
    else:
        return f"catalog/icons/{instance.category}/{filename}"


class Category(models.Model):
    title = models.CharField(max_length=128, db_index=True)
    active = models.BooleanField(default=False)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, blank=True, null=True, related_name="subcategories")
    favourite = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = "pk",

    def href(self):
        """
        Получение ссылки
        :return: ссылка
        """
        return f"/catalog/{self.pk}"

    def __str__(self):
        return self.title


class CategoryIcon(models.Model):

    src = models.FileField(upload_to=category_image_directory_path, max_length=500)
    category = models.OneToOneField(Category, on_delete=models.CASCADE, related_name="image", blank=True, null=True)

    class Meta:
        verbose_name = "Category icon"
        verbose_name_plural = "Category icons"
        ordering = ["pk"]
        
    def alt(self):
        return self.category.title
    
    def href(self):
        return self.src

    def __str__(self):
        return f"icon of {self.category.title}"

