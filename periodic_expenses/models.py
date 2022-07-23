from django.db import models


class Periodic(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Periodic"


class PeriodicPayed(models.Model):
    periodic = models.ForeignKey(Periodic, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    bill_photo = models.FileField(upload_to="media/", blank=True)
    payment_photo = models.FileField(upload_to="media/", blank=True)

    def __str__(self):
        return self.periodic

    class Meta:
        verbose_name_plural = "PeriodicPayed"
