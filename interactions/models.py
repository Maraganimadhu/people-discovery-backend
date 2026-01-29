from django.db import models
from django.contrib.auth.models import User

class Interaction(models.Model):
    INTERACTION_CHOICES = [
        ('INTEREST', 'Interest'),
        ('SKIP', 'Skip'),
    ]

    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_interactions'
    )
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_interactions'
    )
    interaction_type = models.CharField(max_length=10, choices=INTERACTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return f"{self.from_user} -> {self.to_user}"
