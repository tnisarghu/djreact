from django.contrib import admin
# Import your model for admin site here
from .models import Learn, LearnName
# Register your models here.
admin.site.register(Learn)
admin.site.register(LearnName)