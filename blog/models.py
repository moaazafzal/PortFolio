from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='image/')


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]+'....'

    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %b %y')


