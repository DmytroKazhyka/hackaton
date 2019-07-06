from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    player = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.player.username