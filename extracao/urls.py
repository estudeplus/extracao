from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('users/', include('extracao.core.urls')),
    path('api/v1/', include(('extracao.api.urls', 'api'), namespace='api')),
    path('admin/', admin.site.urls),
]
