from django.db import models


class Game(models.Model):
    attempts = models.IntegerField()

    def __str__(self):
        return str(self.attempts)