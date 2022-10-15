from django.db import models

# Create your models here.
class List(models.Model):
    lists = models.TextField()
    def __str__(self):
        return self.lists

class Item(models.Model):
    todos = models.CharField(max_length=100)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    def __str__(self):
        return self.todos