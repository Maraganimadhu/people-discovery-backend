from django.urls import path
from .views import create_interaction

urlpatterns = [
    path('', create_interaction),
]
