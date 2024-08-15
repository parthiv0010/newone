from django.db import models

# Create your models here.
class Destinations(models.Model):
    Title=models.CharField(max_length=200)
    Relesedate=models.CharField(max_length=200)
    Actors=models.CharField(max_length=200)
    Reviews=models.CharField(max_length=200)
    image = models.ImageField(upload_to='destimages/')
    description = models.TextField()
