from django.contrib import admin
from .models import blog, Tag, BlogComment

# Register your models here.
admin.site.register(blog)
admin.site.register(Tag)
admin.site.register(BlogComment)