from django.urls import path

from . import views

urlpatterns = [
    path('', views.menu),
    path('say-hello/', views.hello),
    path('staff-list/', views.staff_list),
]