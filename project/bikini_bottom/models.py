# from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
class Facility(models.Model):

    TYPE_CHOICES = [
        ('government', 'Pemerintahan'),
        ('public_facility', 'Fasilitas Umum'),
        ('park', 'Taman'),
        ('house', 'Perumahan'),
        ('restaurant', 'Restoran')
    ]

    STATUS_CHOICES = [
        ('proposed', 'Proposed'),
        ('under_review', 'Under Review'),
        ('planned', 'Planned'),
        ('cancelled', 'Cancelled'),
        ('construction', 'Under Construction'),
        ('completed', 'Completed')
    ]

    PRICE_CHOICES = [
        ('hourly', 'Per jam'),
        ('daily', 'Per hari'),
        ('weekly', 'Per minggu'),
        ('montly', 'Per bulan'),
        ('annual', 'Per tahun')
    ]

    name = models.CharField(max_length=50)
    types = models.CharField(max_length=20, choices=TYPE_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Proposed')
    open = models.BooleanField(default=False)
    location = models.PointField(srid=4326, spatial_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_unit = models.CharField(max_length=15, choices=PRICE_CHOICES)
    photo = models.ImageField(upload_to='facility')
    operator = models.ForeignKey(User, on_delete=models.CASCADE)
