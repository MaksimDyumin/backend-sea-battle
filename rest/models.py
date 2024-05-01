from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser

class GameUser(AbstractUser):
    pass

class Board(models.Model):
    player = models.OneToOneField(GameUser, on_delete=models.CASCADE, related_name='board')

class Ship(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='ships')

class Cell(models.Model):
    EMPTY = "  "
    SHIP = "S "
    SHIP_HIT = "SX"
    MISS = " X"
    
    STATE_CHOICES = [
        (EMPTY, 'empty'),
        (SHIP, 'ship'),
        (SHIP_HIT, 'ship hit'),
        (MISS, 'miss'),
    ]
    
    state = models.CharField(max_length=2, choices=STATE_CHOICES, default=EMPTY)
    coordinate_y = models.IntegerField()
    coordinate_x = models.IntegerField()
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='cells')
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE, related_name='cells', null=True, blank=True)

