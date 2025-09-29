from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('login.urls')), 
]

##python manage.py runserver 0.0.0.0:8000