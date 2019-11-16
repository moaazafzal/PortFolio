from django.db import models


class Job(models.Model):
    title=0

    image = models.ImageField(upload_to='image/')
    summary = models.CharField(max_length=200)
    title = models.CharField(max_length=100, default='SOME STRING')

    def __str__(self):
        return self.title
