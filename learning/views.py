
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from serializers import UserSerializer, SnippetSerializer
from models import Snippet
from permissions import IsOwnerOrReadOnly

# Create your views here.
class SnippetViewSet(ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (DjangoModelPermissions, IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
