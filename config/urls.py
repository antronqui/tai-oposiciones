"""
URL configuration for config project.
Proyecto TAI 2027
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Allauth accounts (Google OAuth2 + Local)
    path('accounts/', include('allauth.urls')),
    
    # TAI Custom Apps
    path('', include('core.urls')),
    path('perfil/', include('accounts.urls')),
    path('temario/', include('temario.urls')),
    path('examenes/', include('examenes.urls')),
    path('estudio/', include('estudio.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
