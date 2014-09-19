from django.contrib import admin

from xcblog.models import BlogCategory, BlogPost

admin.site.register(BlogCategory)
admin.site.register(BlogPost)