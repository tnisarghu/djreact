import datetime
from django.db import models
from django.utils import timezone
from django.db.models import Q


# Create your models here.
class LearnQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)

    def search(self, query):
        lookup = (
                    Q(name__icontains=query) |
                    Q(description__icontains=query) |
                    Q(sub_topic__icontains=query)
                    )

        return self.filter(lookup)


class LearnManager(models.Manager):
    def get_queryset(self):
        return LearnQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().all().search(query)


class Learn(models.Model):
	name = models.CharField(max_length=40)
	description = models.TextField(null='True', blank='True')
	contentUrl = models.URLField(null='True', blank='True')
	subject = models.CharField(max_length=25, null='True', blank='True', default='Pathology')
	system = models.CharField(max_length=45, null='True', blank='True', default='Renal')
	main_topic = models.CharField(max_length=45, null='True', blank='True')
	sub_topic = models.CharField(max_length=45, null='True', blank='True')
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = LearnManager()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):   # useful to see Learn.name in admin site
		return self.name