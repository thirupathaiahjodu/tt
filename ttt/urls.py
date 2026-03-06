from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('hi/',views.home),
    path('about/',views.about),
    path('add/', views.add_student),
    path('login/', views.login),

]