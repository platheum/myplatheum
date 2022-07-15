from django.db import models


class Suscribtion(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now=True)
