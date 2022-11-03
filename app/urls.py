from django.urls import path
from app import views

urlpatterns= [
    path('', views.job_list, name='jobs_list'),
    path('job/<slug:slug>', views.job_detail, name='job_detail'),
    path('create/', views.job_create, name='job_create'),

]