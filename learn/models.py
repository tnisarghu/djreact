from django.db import models

# Create your models here.
class Learn(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    contentUrl = models.URLField()
    pub_date = models.DateTimeField('date published')
