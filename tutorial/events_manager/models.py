from django.db import models

class Event(models.Model):
    title = models.CharField("title", max_length=240)
    location = models.CharField("location", max_length=240)
    description = models.CharField("description", max_length=960)

    def __str__(self):
        return self.title
