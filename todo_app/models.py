from django.db import models

class Todo_list(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)

    def __str__(self):
        return self.title

