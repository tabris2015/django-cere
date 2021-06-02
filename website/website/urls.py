from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('hello/', include('hello_app.urls')),
    path('students/', include('students.urls')),
    path('admin/', admin.site.urls),
]
