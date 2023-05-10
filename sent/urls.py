from django.urls import path

from .views import home, get_sent_response

urlpatterns = [
    path("", home, name="home"),
    path('get_ner_response/', get_sent_response, name='get_sent_response'),
]