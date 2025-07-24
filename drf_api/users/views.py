from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView

from app.users.models import User
from .serializers import UserSerializer


class UsersApiView(CreateAPIView, RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
