from django.db import models

# Create your models here.

class Emotion(models.Model):
    emotion = models.IntegerField(default = 0)
    timestamp = models.DateTimeField(auto_now_add = True)
    email = models.EmailField()

    class Meta:
        indexes = [
            models.Index(fields= ['email']),
            models.Index(fields= ['emotion'])
        ]
