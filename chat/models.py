from django.db import models

class registerUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
      
class Chat_Room(models.Model):
    room_name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    onlineUsers = models.ManyToManyField(registerUser, related_name="onlineUsers") 
    

    def __str__(self):
        return self.room_name
      
      
      
class Chat_Message(models.Model):
    user_name = models.ForeignKey(registerUser, on_delete=models.CASCADE) 
    room_name = models.ForeignKey(Chat_Room, on_delete=models.CASCADE)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message
      


      
      