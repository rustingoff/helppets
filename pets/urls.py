from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sub/', views.get_subscription, name='get_subscription'),
]
