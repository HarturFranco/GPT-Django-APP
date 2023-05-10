from django.urls import path

from .views import home, get_chat_response

urlpatterns = [
    path("", home, name="home"),
    path('get_chat_response/', get_chat_response, name='get_chat_response'),
]