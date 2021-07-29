from django.contrib import admin
from django.urls import path, include
from fireapp import views as fireapp_views


admin.site.site_title=" Reskill wildfire"
admin.site.site_header="Reskill Wildifre Project"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fireapp.urls')),
]

handler404 = 'fireapp.views.error_404'

