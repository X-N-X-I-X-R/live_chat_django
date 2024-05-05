# live_chat_django

-  run the project
>  daphne ChatApp.asgi:application
> redis-server --port 6380  


#  if have any issue kill and find  the open ports  with linux command 
> lsof -i :<port> 
> kill -9 <Prcessid>


# Roadmap --> How to create a chat application using Django Channels and Redis 

1- pip install channels  
///  Django Channels is a project that takes Django and extends its abilities beyond HTTP - to handle WebSockets, chat protocols, IoT protocols, and more.

2 - pip install channels_redis 
/// This package provides a channel layer that uses Redis as its backing store. It enables you to use Redis as a message broker to handle messages between Django instances, and to store the messages in Redis. 

3 -pip install redis 
/// Redis is an open-source, in-memory data structure store, used as a database, cache, and message broker.

4- pip install daphne -
/// Daphne is a HTTP, HTTP2, and WebSocket protocol server for ASGI and ASGI-HTTP, developed as part of the Django Channels project. It supports automatic negotiation of protocols; there's no need for URL prefixing to determine WebSocket endpoints versus HTTP endpoints.



# add to settings.py 
-  inside installed apps --> 'channels', 'channels_redis'
-  add the following code to the bottom of the settings.py file

ASGI_APPLICATION = 'ChatApp.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('
            ', 6380)],},  },}



# create a new file called asgi.py in the same directory as settings.py and add the following code
asgi is a standard for Python asynchronous web applications and servers to communicate with each other.
It enables an application server to communicate with a web server, and vice versa, over a network connection. 

# create a new file called routing.py in the same directory as settings.py and add the following code
-  routing.py is used to define the routing configuration for the Django Channels application. 
-  It specifies which consumers should receive messages from which channels, and how to handle those messages.

# create a new file called consumers.py in the same directory as settings.py and add the following code
-  consumers.py is used to define the consumers for the Django Channels application.
-  Consumers are classes that handle WebSocket connections and messages, and can be used to implement chat functionality, real-time updates, and more.

