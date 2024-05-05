from atexit import register
from django.contrib import admin

from .models import USERS, Chat_Room, Chat_Message

admin.site.register(USERS)
admin.site.register(Chat_Room)
admin.site.register(Chat_Message)