from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=30)

class Board(models.Model):
    player = models.OneToOneField(User, on_delete=models.CASCADE, related_name='board')

class Cell(models.Model):
    isShip = models.BooleanField()
    isShooted = models.BooleanField()
    coordinateY = models.IntegerField()
    coordinateX = models.IntegerField()
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='cell')

