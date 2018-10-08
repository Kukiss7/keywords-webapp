from django.db import models

class Website(models.Model):
    url = models.CharField(max_length=255)
    keywords = models.CharField(max_length=1200)
