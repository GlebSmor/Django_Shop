from django.db import models
from django.contrib.auth.models import User


def avatar_image_directory_path(instanse: "Avatar", filename):
    return f"avatars/images/{instanse.profile.pk}/{filename}"


class Avatar(models.Model):
    profile = models.OneToOneField("Profile", verbose_name='avatar', on_delete=models.CASCADE)
    image = models.FileField(upload_to=avatar_image_directory_path)
    
    class Meta:
        verbose_name = "Profile image"
        verbose_name_plural = "Profile images"
        ordering = ["pk",]
        
    def src(self):
        return f"/media/{self.image}"
    
    def alt(self):
        return f"{self.profile.user.username}_avatar"

    def __str__(self):
        return f"{self.profile.user.username}_avatar"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    fullName = models.CharField(max_length=256, null=False, blank=True, default='')
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=64)
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ["pk",]
        
    def __str__(self):
        return f"{self.user.username}_profile"
