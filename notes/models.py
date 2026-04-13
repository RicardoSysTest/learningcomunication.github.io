from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notes"
    )
