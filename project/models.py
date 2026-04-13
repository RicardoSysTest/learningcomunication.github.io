from django.db import models

"""
Due Data: December 10, 2020
Project Name: Web Designing
Status: Prototyping
Progress: 60%
Background-color: #ff942e"
Participants:images
Days Left: 2 
"""
# Create your models here.


class Projects(models.Model):

    # Status
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PROTO = 'prototypes', 'Prototypes'
        DEV = 'development', 'Development'
        REV = 'review', 'Review'

    status = models.CharField(
        blank=Status.DRAFT, choices=Status.choices, max_length=20)
    title = models.CharField(max_length=200)

    # Content of Project
    text = models.TextField()

    # Due Date
    created = models.DateField()

    # Progress
    progress = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Background-color
    # Participants
    # Days Left
