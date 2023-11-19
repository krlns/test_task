from django.contrib.auth.models import User
from django.db import models


class Cats(models.Model):
    HAIRINESS_CHOICES = [
        ("s", "маленькая"),
        ("m", "средняя"),
        ("l", "высокая")
    ]

    name = models.CharField(max_length=30)
    age = models.IntegerField()
    breed = models.CharField(max_length=30)
    hairiness = models.CharField(max_length=30, choices=HAIRINESS_CHOICES)
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
