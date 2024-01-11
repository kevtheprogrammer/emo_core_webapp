from django.db import models
from account.models import User


class ServiceCategory(models.Model):
    cover = models.ImageField(
        upload_to="category/cover/", default="category.png")
    name = models.CharField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Service(models.Model):
    name = models.CharField()
    category = models.ForeignKey(
        ServiceCategory, on_delete=models.CASCADE, related_name="service_category", default=None)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Project(models.Model):
    cover = models.ImageField(upload_to="products/thum/",
                              blank=True, verbose_name="first image")
    name = models.CharField()
    info = models.TextField()
    link = models.URLField(default='https://')
    img1 = models.ImageField(upload_to="products/thum/",
                             blank=True, verbose_name="first image")
    img2 = models.ImageField(upload_to="products/thum/",
                             blank=True, verbose_name="second image")
    img3 = models.ImageField(upload_to="products/thum/",
                             blank=True, verbose_name="third image")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class workExperience(models.Model):
    position = models.CharField()
    company = models.CharField()
    info = models.TextField()
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    employee = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None
    )

class Education(models.Model):
    certification = models.CharField()
    organization = models.CharField()
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    student = models.ForeignKey (
        User, on_delete=models.CASCADE, default=None
    )

class Portifolio(models.Model):
    "hire me profile"
    about = models.TextField()
    expectation = models.CharField()
    services = models.ManyToManyField(Service)
    projects = models.ManyToManyField(Project)
    seeker = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None
    )
    education = models.ManyToManyField(
        Education
    )
    work = models.ManyToManyField(
        workExperience, on_delete=models.CASCADE, default=None
    )
    cv = models.FileField(upload_to='portifplio/')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
