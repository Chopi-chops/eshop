from django.db import models

# Create your models here.
class New(models.Model):
    title = models.CharField(max_length=1000)
    article = models.TextField(null=True, blank=True)
    views = models.IntegerField()

    def __str__(self):
        return self.title
