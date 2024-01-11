from django.db import models
from django.urls import reverse
# from django_countries.fields import CountryField

from account.models import User
from .managers import ProductManager


class Category(models.Model):
    cover = models.ImageField(
        upload_to="category/cover/", default="category.png")
    title = models.CharField(max_length=700)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default=None)

    def __str__(self) -> str:
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('product:category-details', args=[self.slug])

    class Meta:
        ordering = ['-updated']


class Tag(models.Model):
    title = models.CharField(max_length=700)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title}'


class Color(models.Model):
    name = models.CharField(max_length=700)
    color_code = models.CharField(max_length=6)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Size(models.Model):
    name = models.CharField(max_length=700)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'


class City(models.Model):
    name = models.CharField(max_length=700)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Province(models.Model):
    name = models.CharField(max_length=700)
    cities = models.ManyToManyField(City)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Product(models.Model):
    """products table"""

    thumb = models.ImageField(
        upload_to="products/thum/", default="products.png")
    name = models.CharField(max_length=900)
    description = models.TextField(verbose_name="product description")
    price = models.DecimalField(
        default=1.0, max_digits=1000, max_length=7, decimal_places=2)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    location_city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="location_city", default=None)
    discount = models.DecimalField(
        default=0.0, max_digits=1000, max_length=7, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category", default=None)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="seller", default=None)
    img1 = models.ImageField(upload_to="products/thum/",
                             blank=True, verbose_name="first image")
    img2 = models.ImageField(upload_to="products/thum/",
                             blank=True, verbose_name="second image")
    img3 = models.ImageField(upload_to="products/thum/",
                             blank=True, verbose_name="third image")
    tags = models.ManyToManyField(Tag, related_name="tags")
    colors = models.ManyToManyField(Color, related_name="colors")
    favourite = models.ManyToManyField(
        User, related_name='favourite', blank=True, default=None)
    is_pub = models.BooleanField(default=False, verbose_name="is published")
    avr_views_duration = models.DurationField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0),
    creation_ip_address = models.CharField(
        max_length=24, default=None, blank=True, null=True)
    deletion_ip_address = models.CharField(
        max_length=24, default=None, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default=None, blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author", default=None)

    objects = ProductManager()

    def __str__(self):
        return f'{self.name}'

#     def get_absolute_url(self):
#         return reverse('product:detail', args=[self.pk, self.slug])

#     def toggle_favourite(self):
#         return reverse('product:favourite-toggle', args=[self.pk])

#     def add_to_cart(self):
#         return reverse('product:add-to-cart', args=[self.pk])

#     def remove_from_cart(self):
#         return reverse('product:remove-from-cart', args=[self.pk])

#     def get_init_price(self):
#         return self.price

#     def get_discount_price(self):
#         pri = self.get_init_price() - self.discount
#         return round(pri, 2)

#     def get_discount_percentage(self):
#         prc = (self.discount / self.get_init_price()) * 100
#         return round(prc, 0)

#     def get_absolute_url_admin(self):
#         return reverse('account:product-detail', args=[self.pk, self.slug])

    class Meta:
        ordering = ['-timestamp']

    # def 404_url
    # def out_of_stock_url
    # def get_price
    # def get_absolute_url
    # def get_discount


class PropertyRequst(models.Model):
    """products table"""

    thumb = models.ImageField(
        upload_to="products/thum/", default="products.png")
    name = models.CharField(max_length=900)
    description = models.TextField(verbose_name="product description")

    cat = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="cat", default=None)
    img1 = models.ImageField(upload_to="products/thum/",
                             blank=True, verbose_name="first image")
    img2 = models.ImageField(upload_to="products/thum/",
                             blank=True, verbose_name="second image")
    img3 = models.ImageField(upload_to="products/thum/",
                             blank=True, verbose_name="third image")
    colors = models.ManyToManyField(Color, related_name="product_colors")

    is_pub = models.BooleanField(default=False, verbose_name="is published")
    is_available = models.BooleanField(
        default=False, verbose_name="is available")
    avr_views_duration = models.DurationField(blank=True, null=True)

    views = models.PositiveIntegerField(default=0),
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default=None, blank=True, null=True)
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customer", default=None)

    objects = ProductManager()


class Review(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'contact by {}'.format(self.name,)
