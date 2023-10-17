from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import uuid

class Form(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Une ID unique pour chaque formulaire de l'app")
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    responses = models.IntegerField(default=0)
    creation_date = models.DateTimeField("Date de création")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('FormPage', args=[str(self.id)])



class Question(models.Model):
    name = models.CharField(max_length=200)
    form = models.ForeignKey('Form', on_delete=models.CASCADE, null=False)
    is_required = models.BooleanField()

    Question_Type = [
        ("C", "Checkboxes"),
        ("R", "Roundboxes"),
        ("T", "Text"),
        ("L", "Linearscale"),
    ]

    type = models.CharField(max_length=1, choices=Question_Type, blank=False, default="T", help_text="Type de question")

    def __str__(self) -> str:
        return f'{self.name}, {self.type}'



class Answer(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=False)


    def __str__(self) -> str:
        return f'{self.text}'

# Faudra faire une classe our les résultats
