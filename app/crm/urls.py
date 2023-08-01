from django.urls import path
from crm import views

urlpatterns = [
    path('', views.index, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('record/create/', views.RecordCreateView.as_view(), name='record-create'),
]