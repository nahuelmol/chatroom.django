from django.contrib import admin

from db.models import Post, Comment, Event

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Event)