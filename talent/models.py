from django.db import models
from users.models import User
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.stage_name)
            slug = base_slug
            counter = 1

            while TalentProfile.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

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