from turtle import title
from django.db import models
from django.utils.timezone import now
from Realtors.models import Realtor


class Listing(models.Model):
    class SaleType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'

    class HomeType(models.TextChoices):
        HOUSE = 'House'
        CONDO = 'Condo'
        TOWNHOUSE = 'Townhouse'
    
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    sale_type = models.CharField(max_length=50, choices=SaleType.choices, default=SaleType.FOR_SALE)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    home_type = models.CharField(max_length=50, choices=HomeType.choices, default=HomeType.HOUSE)
    sqft = models.IntegerField()
    open_house = models.BooleanField(default=False)
    photo_main = models.BooleanField(default=False)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_11 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_12 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_13 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_14 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_15 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_16 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_17 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_18 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_19 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_20 = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)


    def __str(self):
        return self.title


