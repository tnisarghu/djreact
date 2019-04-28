import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Learn(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    contentUrl = models.URLField()
    pub_date = models.DateTimeField('date published')

    def __str__(self): # usefull to see Learn.name in admin site
        return self.name

    def was_published_recently(self): # check weather the learn is not published recently
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

		
class LearnName(models.Model):
	name = models.ForeignKey(Learn, on_delete=models.CASCADE)
	subject = models.CharField(max_length=20)
	main_topic = models.CharField(max_length=45)
	sub_topic = models.CharField(max_length=45)
	pub_date = models.DateTimeField('date published')
	timestamp = models.DateTimeField(auto_now_add=True)
