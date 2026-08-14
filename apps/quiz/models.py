from django.db import models


class Fairy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="fairies/", blank=True, null=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers",
    )
    text = models.CharField(max_length=255)
    fairy = models.ForeignKey(
        Fairy,
        on_delete=models.CASCADE,
        related_name="answers",
    )

    def __str__(self):
        return self.text