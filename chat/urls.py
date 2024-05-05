from django.urls import path, include
from chat import views as chat_views


urlpatterns = [
    path('login/', chat_views.login_view, name='login_view'),
   path("register_view/", chat_views.register_view, name="register-page"), 

    path("chat/", chat_views.chatPage, name="chat-page"), # type: ignore
]