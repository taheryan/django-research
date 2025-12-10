from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('members.urls', namespace='members')),
    path('api/', include('members.api.urls')),  # DRF API endpoints
]