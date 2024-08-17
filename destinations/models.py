from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Destinations(models.Model):
    Title=models.CharField(max_length=200)
    Relesedate=models.CharField(max_length=200)
    Actors=models.CharField(max_length=200)
    Reviews=models.CharField(max_length=200)
    image = models.ImageField(upload_to='destimages/')
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

class Review(models.Model):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveIntegerField()  # Rating out of 5 or any other scale
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.destination.Title}"


    class Meta:
        ordering = ['-created_at']


