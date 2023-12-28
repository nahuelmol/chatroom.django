from django.contrib import admin

from db.models import Post, Comment, Event, Follower, Subscriber, Moderator

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Event)

admin.site.register(Follower)
admin.site.register(Subscriber)
admin.site.register(Moderator)