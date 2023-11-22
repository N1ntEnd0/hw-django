from django.db import models


# Create your models here.
class Review(models.Model):
    fullName = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=50, blank=False)
    text = models.CharField(max_length=1000, blank=False)
    checked = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return f'{self.fullName} - {self.checked}'
