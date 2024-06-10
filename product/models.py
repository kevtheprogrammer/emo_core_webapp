from django.db import models
from django.urls import reverse

from account.models import User
from .managers import ProductManager


class Category(models.Model):
    cover = models.ImageField(upload_to="category/cover/", default="category.png")
    title = models.CharField(max_length=700)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default=None, unique=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('product:category-details', args=[self.slug])

    class Meta:
        ordering = ['-updated']


class Tag(models.Model):
    title = models.CharField(max_length=700)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Color(models.Model):
    name = models.CharField(max_length=700)
    color_code = models.CharField(max_length=6)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=700)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    name = models.CharField(max_length=700)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=700)
    cities = models.ManyToManyField(City)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    """products table"""

    thumb = models.ImageField(upload_to="products/thumb/", default="products.png")
    name = models.CharField(max_length=900)
    description = models.TextField(verbose_name="product description")
    price = models.DecimalField(default=1.0, max_digits=10, decimal_places=2)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    location_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="products", default=None)
    discount = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", default=None)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products", default=None)
    img1 = models.ImageField(upload_to="products/images/", blank=True, verbose_name="first image")
    img2 = models.ImageField(upload_to="products/images/", blank=True, verbose_name="second image")
    img3 = models.ImageField(upload_to="products/images/", blank=True, verbose_name="third image")
    tags = models.ManyToManyField(Tag, related_name="products")
    colors = models.ManyToManyField(Color, related_name="products")
    favourite = models.ManyToManyField(User, related_name='favourites', blank=True)
    is_pub = models.BooleanField(default=False, verbose_name="is published")
    avr_views_duration = models.DurationField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    creation_ip_address = models.CharField(max_length=24, blank=True, null=True)
    deletion_ip_address = models.CharField(max_length=24, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default=None, blank=True, null=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="authored_products", default=None)

    objects = ProductManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-timestamp']


class PropertyRequest(models.Model):
    thumb = models.ImageField(upload_to="products/thumb/", default="products.png")
    name = models.CharField(max_length=900)
    description = models.TextField(verbose_name="product description")
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="property_requests", default=None)
    img1 = models.ImageField(upload_to="products/images/", blank=True, verbose_name="first image")
    img2 = models.ImageField(upload_to="products/images/", blank=True, verbose_name="second image")
    img3 = models.ImageField(upload_to="products/images/", blank=True, verbose_name="third image")
    colors = models.ManyToManyField(Color, related_name="property_requests")
    is_pub = models.BooleanField(default=False, verbose_name="is published")
    is_available = models.BooleanField(default=False, verbose_name="is available")
    avr_views_duration = models.DurationField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default=None, blank=True, null=True, unique=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="property_requests", default=None)

    objects = ProductManager()


class Review(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews", default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Review by {self.name}'
