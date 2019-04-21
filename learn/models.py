import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Learn(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    contentUrl = models.URLField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
