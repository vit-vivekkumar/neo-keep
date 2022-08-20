from django.db import models

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=200)
  note = models.CharField(max_length=140, default='')
      
  def __str__(self):
    return self.title
