from django.db import models
from django.contrib.auth.models import AbstractUser

class GameUser(AbstractUser):
    pass
class Board(models.Model):
    player = models.OneToOneField(GameUser, on_delete=models.CASCADE, related_name='board')

class Cell(models.Model):
    is_ship = models.BooleanField()
    is_shooted = models.BooleanField()
    coordinate_y = models.IntegerField()
    coordinate_x = models.IntegerField()
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='cells')
