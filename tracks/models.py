from django.db import models

class Track(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_per_hour = models.IntegerField(default=0)
    length_km = models.FloatField(default=0)
    image = models.ImageField(upload_to='tracks/', blank=True, null=True)

    def __str__(self):
        return self.name
# Create your models here.
