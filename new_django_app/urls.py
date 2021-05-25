from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.home, name='new_django_app-home'),
    path('about/', views.about, name='new_django_app-about'),
]
