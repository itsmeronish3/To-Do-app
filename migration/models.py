from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
