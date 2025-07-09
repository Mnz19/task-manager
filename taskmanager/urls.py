from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Apps
    path('api/core/', include('apps.core.urls')),
    path('api/notifications/', include('apps.notifications.urls')),
    path('api/shared/', include('apps.shared.urls')),
    path('api/tasks/', include('apps.tasks.urls')),
    path('api/teams/', include('apps.teams.urls')),
    path('api/users/', include('apps.users.urls')),
]
