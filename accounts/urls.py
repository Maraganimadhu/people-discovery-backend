from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', views.register, name='accounts-register'),
    path('login/', TokenObtainPairView.as_view(), name='accounts-login'),
    

]
