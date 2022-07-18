from distutils.command.upload import upload
import email
from statistics import mode
#from tkinter.tix import Tree
from django.db import models
from datetime import datetime
from django.utils import timezone


class Realtor(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    top_seller = models.BooleanField(default=False)
    date_hired = models.DateTimeField(default=timezone.now, blank=True)


    def __str__(self):
        return self.name