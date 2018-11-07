from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='rank-home'),
    path('about/', views.about, name='rank-about'),
]
