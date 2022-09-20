from django.urls import path

# local modules
from . import views

urlpatterns = [
    path('api/login/', views.login),
    # localhost:8000/api/login/
    path('api/register/', views.register),
    # localhost:8000/api/register/
]