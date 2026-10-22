from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [path('', views.home, name = 'home'),
               path('photo/<int:pk>', views.photo_detail, name = 'photo_detail')]