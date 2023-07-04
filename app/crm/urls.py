from django.urls import path
from crm import views

urlpatterns = [
    path('', views.index, name='home'),
    path('logout/', views.logout, name='logout'),
]