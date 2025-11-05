from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import AboutView

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔹 Rutas principales de la web
    path('', views.home, name='home'),
    path('cars/', include('cars.urls')),
    path('accounts/', include('accounts.urls')),
    path('about/', views.about, name='about'),
    path('messages/', include('messages_app.urls')),
]

# 🔹 Archivos estáticos y de medios
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
