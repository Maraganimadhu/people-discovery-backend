from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Tech'),
        ('sports', 'Sports'),
        ('music', 'Music'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # age = models.PositiveIntegerField()
    age = models.IntegerField(null=True, blank=True)

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    bio = models.CharField(max_length=250)
    last_active = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        
