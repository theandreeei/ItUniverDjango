from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('pet', views.pet),
    path('aboutme/', views.about)  # Зі / чомусь вибивало помилку 404, хоча pet робить і без /.
]
