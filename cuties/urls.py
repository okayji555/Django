from django.urls import path
from . import views

urlpatterns = [
    path('cuties/', views.cuties, name='cuties'),
]
