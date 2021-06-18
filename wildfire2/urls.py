from wildfire2.settings import MEDIA_ROOT
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from fireapp import views as fireapp_views
import fireapp


admin.site.site_title=" Reskill wildfire"
admin.site.site_header="Reskill Wildifre Project"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fireapp_views.index, name="homepage"),
    path('fireapp/', include('fireapp.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

