from django.db import models

class App(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
