from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.title} from {self.year}'
