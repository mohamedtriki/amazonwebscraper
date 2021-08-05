from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from scraper_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('api/',include('scraper_app.urls')),
]
urlpatterns+= staticfiles_urlpatterns()          
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)