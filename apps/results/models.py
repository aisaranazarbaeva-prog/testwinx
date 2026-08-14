from django.db import models
from django.contrib.auth.models import User
from apps.quiz.models import Fairy

class Result(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="results"
    )
    fairy = models.ForeignKey(
        Fairy,
        on_delete=models.CASCADE,
        related_name="results"
    )
    score = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} — {self.fairy.name}"