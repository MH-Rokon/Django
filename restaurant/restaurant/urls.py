
from django.contrib import admin
from django.urls import path,include
from meal import views
from about_us import viewss

urlpatterns = [
    path('admin/', admin.site.urls),
    path('meal/', include('meal.urls')),
    path('about_us/', include('about_us.urls')),
    path('home/',views.home, name='home'),
    # path('', views.home, name='home'),
    path('showitem/', views.showitem, name='showitem'),
    path('menu/', views.menu, name='menu'),
     path('about/', viewss.about, name='about'),
]
