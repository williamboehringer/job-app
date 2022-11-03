from urllib.parse import urlparse
from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
