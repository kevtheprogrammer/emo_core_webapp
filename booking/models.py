from django.db import models


class Events(models.Model):
    
    title = models.CharField(max_length=700)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    barner = models.ImageField(upload_to='events/barner/')
    img = models.ImageField(upload_to='events/barner/', blank=True, null=True)
    img2 = models.ImageField(upload_to='events/barner/', blank=True, null=True)
    price = models.DecimalField(
        default=1.0, max_digits=1000, max_length=7, decimal_places=2)
    description = models.TextField(verbose_name="event description")
    location = models.CharField(max_length=700)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
