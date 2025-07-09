from rest_framework import viewsets, permissions
from apps.users.models.user import User
from apps.users.serializers.user import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    
    def get_queryset(self):
        return self.queryset.filter(is_active=True)
