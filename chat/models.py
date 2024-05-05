from django.db import models
from django.contrib.auth.models import User

class USERS(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)

    
    def __str__(self):
        return self.username.username

class Chat_Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=50)
    room_description = models.TextField()
    users_in_room = models.ManyToManyField(USERS) 
    
    def __str__(self):
        return self.room_name

class Chat_Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    message_content = models.TextField()
    message_time = models.DateTimeField(auto_now_add=True)
    message_sender = models.ForeignKey(USERS, on_delete=models.CASCADE)
    message_room = models.ForeignKey(Chat_Room, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.message_content