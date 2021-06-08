from django.urls import path
from . import views

app_name = 'authentication'
urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('log_user/', views.login_user, name='login')
]
