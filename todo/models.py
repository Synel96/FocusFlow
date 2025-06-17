from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)

def __str__(self):
        return self.title