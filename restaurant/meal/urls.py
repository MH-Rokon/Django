from django.urls import path
from meal import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('showitem/', views.showitem, name='showitem'),
    path('menu/', views.menu, name='menu'),
    
]
