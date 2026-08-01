from django.contrib import admin

from db.models import Post, Comment, Event, Follower, Suscriptor, Moderator, Notification

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Event)

admin.site.register(Follower)
admin.site.register(Suscriptor)
admin.site.register(Moderator)
admin.site.register(Notification)
