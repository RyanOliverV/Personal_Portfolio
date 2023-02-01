from django.contrib import admin
from .models import Post, Contact, Comment

# Allows the Admin page to access the models
admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Comment)
