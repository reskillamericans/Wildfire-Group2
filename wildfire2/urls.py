from django.contrib import admin
from django.urls import path, include
from fireapp import views as fireapp_views


admin.site.site_title=" Reskill wildfire"
admin.site.site_header="Reskill Wildifre Project"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fireapp_views.index, name="homepage"),
    path('', include('fireapp.urls')),
]