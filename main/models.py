from audioop import reverse
from django.db import models


class Car(models.Model):
    MECHANIC, AUTO, ROBOT = range(3)
    KPP_CHOICES = [
        [MECHANIC, "Механическая коробка передач"],
        [AUTO, "Автоматическая коробка передач"],
        [ROBOT, "Роботизированная коробка передач"],
    ]
    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    kpp = models.SmallIntegerField(choices=KPP_CHOICES)
    color = models.CharField(max_length=255)
    img = models.ImageField()
    slug = models.SlugField(unique=True, auto_created=True, db_index=True)
    
    def __str__(self):
        return self.model    
    
    def get_absolute_url(self):
        return reverse("car", kwargs={"car_slug": self.slug})