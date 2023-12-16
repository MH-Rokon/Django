from django.urls import path
from about_us import viewss

urlpatterns = [
    path('about/', viewss.about, name='about'),
]
