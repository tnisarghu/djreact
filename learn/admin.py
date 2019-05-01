from django.contrib import admin
# Import your model for admin site here
from .models import Learn, LearnName
# Register your models here.
class LearnInline(admin.TabularInline):
    model = LearnName
    extra = 0


class LearnAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'description', 'contentUrl']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [LearnInline]
    list_display = ('name', 'pub_date')
    ordering = ['pub_date']
    search_fields = ['name']


class LearnNameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Subject', {'fields': ['subject', 'system', 'main_topic', 'sub_topic'], 'classes': ['collapse']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]
    list_display = ('name', 'subject', 'system', 'main_topic', 'sub_topic')
    # search_fields = ['name', 'subject', 'system', 'main_topic', 'sub_topic'] not works
    search_fields = ['subject', 'system', 'main_topic', 'sub_topic']

admin.site.register(Learn, LearnAdmin)
admin.site.register(LearnName, LearnNameAdmin)