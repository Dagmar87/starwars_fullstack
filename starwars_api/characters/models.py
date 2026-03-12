from django.db import models

class Character(models.Model):
  name = models.CharField(max_length=200)
  height = models.IntegerField(null=True, blank=True)
  mass = models.IntegerField(null=True, blank=True)
  gender = models.CharField(max_length=20)
  birth_year = models.CharField(max_length=20)
  
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
		  return self.name