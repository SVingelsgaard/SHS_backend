from django.db import models



class TimeValue(models.Model):
    time = models.CharField(max_length=5)  # Store time as string in "hh:mm" format

    def __str__(self):
        return self.time

class BusTime(models.Model):
    location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    bus_number = models.CharField(max_length=20)
    times = models.CharField(max_length=100)

    def __str__(self):
        return f"Bus Time {self.id}"

