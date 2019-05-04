from django.contrib import admin
# Import your model for admin site here
from .models import Learn
# Register your models here.


class LearnAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'description', 'contentUrl']}),('Subject', {'fields': ['subject', 'system', 'main_topic', 'sub_topic'], 'classes': ['collapse']}),]
    list_display = ('name', 'subject', 'system', 'main_topic', 'sub_topic')
    ordering = ['name']
    search_fields = ['name','main_topic', 'sub_topic']


admin.site.register(Learn, LearnAdmin)