from django.db import models
from users.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
class TalentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    stage_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    city = models.CharField(max_length=100)
    price_from = models.DecimalField(max_digits=10, decimal_places=2)
    profile_image = models.URLField(blank=True, null=True)
    rating = models.FloatField(default=0)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.stage_name