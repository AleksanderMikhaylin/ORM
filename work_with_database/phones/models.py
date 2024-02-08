# print('phones/models.py')
from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50, db_index=True, verbose_name="done")

