from django.db import models

# Create your models here.


class Task(models.Model):

    task_name = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Task")
        verbose_name_plural = ("Tasks")

    def __str__(self):
        return self.task_name

  