from django.db import models
from django.contrib.auth.models import User
from tracks.models import Track

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    total_price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.track} - {self.date}"
# Create your models here.
