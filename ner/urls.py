from django.urls import path

from .views import home, get_ner_response

urlpatterns = [
    path("", home, name="home"),
    path('get_ner_response/', get_ner_response, name='get_ner_response'),
]