from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fireapp.urls')),
]

handler404 = 'fireapp.views.error_404'

