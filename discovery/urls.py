from django.urls import path
from .views import discover_people

urlpatterns = [
    path('people/', discover_people),
]
