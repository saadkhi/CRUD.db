from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.login, name='login'),
]