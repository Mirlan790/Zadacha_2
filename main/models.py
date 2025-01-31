from django.db import models


class Task(models.Model):
    title = models.CharField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    data = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)


    def __str__(self):
        return self.name
