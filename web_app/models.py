from django.db import models
from django.contrib.auth.models import User

class todolist(models.Model):
    name = models.CharField(max_length=255)
    due_date = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=100)
    assigned_to = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name