from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Quiz_User(User):
    class Meta:
        verbose_name_plural = 'Quiz_User'
    score = models.IntegerField(default=0)
