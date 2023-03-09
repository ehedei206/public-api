from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    def __str__(self) -> str:
        return self.name
    
    name = models.CharField(max_length=150, unique=True)
    users = models.ManyToManyField(User, blank=True)

class Column(models.Model):
    def __str__(self) -> str:
        return self.board.name+"/"+self.name
    
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

class Ticket(models.Model):
    def __str__(self) -> str:
        return self.column.name+"/"+self.title
    
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    column = models.ForeignKey(Column, on_delete=models.CASCADE)