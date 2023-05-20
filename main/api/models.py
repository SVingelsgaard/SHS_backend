from django.db import models
class BusTime(models.Model):
    time = models.DateTimeField()
    where = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    bus_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Bus Time {self.id}"