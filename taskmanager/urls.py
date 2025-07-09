from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Auth
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # Apps
    path('api/', include('apps.core.urls')),
    path('api/', include('apps.notifications.urls')),
    path('api/', include('apps.shared.urls')),
    path('api/', include('apps.tasks.urls')),
path('api/', include('apps.teams.urls')),
    path('api/', include('apps.users.urls')),
]
