from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
    path('', views.menu, name='menu'),
    path('say-hello/', views.hello),
    path('staff-list/', views.staff_list, name='staff_list'),
    path('staff-details/<int:id>', views.staff_details, name='staff_details'),
]