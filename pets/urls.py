from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('donate/<int:id>/', views.donate, name='donate'),
    path('sub/', views.get_subscription, name='get_subscription'),
]
