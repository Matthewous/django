from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.TextField()
    release_date = models.DateField()
    slug = models.SlugField(max_length=30)

