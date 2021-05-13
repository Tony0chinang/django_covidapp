from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from main import views

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('top/confirmed', views.TopConfirmedCases .as_view(), name='top-confirmed'),
    path('get/top/confirmed/', views.search, name='search'),
    path('cleardata/', views.clearData, name='cleardata'),
    path('', views.home, name='home'),
    path('api/', include(router.urls)),    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)