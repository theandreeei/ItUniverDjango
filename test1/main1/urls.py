from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('pet', views.pet),
    path('fullname', views.fullname),
    path('place', views.place),
    path('years_old', views.years_old),
    path('education', views.education),
    path('hobby', views.hobby),
    path('else_about_me', views.else_about_me),
]

