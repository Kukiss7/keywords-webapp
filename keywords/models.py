from django.db import models

class Website(models.Model):
    url = models.CharField(max_length=255)
    keywords = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    