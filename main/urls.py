from django.urls import path
from . import views

#These url patterns setup the mapping, and sends the users to the correct locations
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]