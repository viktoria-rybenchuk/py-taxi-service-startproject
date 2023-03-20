from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=63)
    country = models.CharField(max_length=63)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name="unique_name",
                fields=["name"]
            )
        ]

    def __str__(self) -> str:
        return f"{self.name}, {self.country}"


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    def __str__(self) -> str:
        return f"{self.manufacturer.name} {self.model}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name="unique_license_number",
                fields=["license_number"]
            )
        ]
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"