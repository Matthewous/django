from django.db import models


class Phone(models.Model):
    name = models.CharField(50)
    price = models.FloatField(2)
    image = models.TextField()
    release_date = models.DateField()
    slug = models.SlugField(max_length=30)

