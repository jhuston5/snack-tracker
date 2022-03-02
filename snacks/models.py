from unicodedata import name
from django.db import models

# Create your models here.

class Snack(models.Model):
  name = models.CharField(max_length=64)
  purchaser = on_delete=models.CASCADE
  description = models.TextField()

  def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name