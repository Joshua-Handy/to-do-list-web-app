from django.db import models

# Create your models here.
class todolist(models.Model):
    name = models.CharField(max_length=255)
    due_date = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=100)
    people_involved = models.CharField(max_length=255)

    def __str__(self):
        return self.name