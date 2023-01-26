from django.db import models

# Create your models here.
class Location(models.Model):
  country = models.CharField(max_length=150)
  city = models.CharField(max_length=150)
  image = models.ImageField(blank=True, upload_to='locations/')
  description = models.CharField(max_length=500, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.country

  class Meta:
    ordering = ['country']


class Spot(models.Model):
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=500, blank=True, null=True)
  address = models.CharField(max_length=250, blank=True, null=True)
  image = models.ImageField(blank=True, upload_to='spots/')
  release_date = models.DateField(blank=True, null=True)
  num_stars = models.IntegerField(blank=True, null=True)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ['name']