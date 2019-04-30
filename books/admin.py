from django.contrib import admin
from .models import Books

# Register your models here.
class BooksAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'chapter', 'sub_chapter', 'topics', 'content']}),
        ('Date information', {'fields': ['publish_date'], 'classes': ['collapse']}),
        ('User', {'fields': ['user'], 'classes': ['collapse']}),
        ('Image', {'fields': ['image'], 'classes': ['collapse']}),
        ('Slug', {'fields': ['slug'], 'classes': ['collapse']}),
    ]
    list_display = ('title', 'chapter', 'sub_chapter', 'topics')
    search_fields = ['title', 'chapter', 'sub_chapter', 'topics', 'content']
    prepopulated_fields = {"slug": ("slug",)}


admin.site.register(Books, BooksAdmin)

''' title = models.TextField()
    chapter = models.TextField()
    sub_chapter = models.TextField()
    topics = models.TextField()
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    slug '''