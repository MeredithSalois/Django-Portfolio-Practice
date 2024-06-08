from django.db import models
from django.core.validators import MinLengthValidator

class Project(models.Model):
    title = models.CharField(max_length=500, validators=[MinLengthValidator(5, "Project names must contain at least 5 characters")])
    detail = models.TextField(default='', max_length=1000)
    collaborators = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
