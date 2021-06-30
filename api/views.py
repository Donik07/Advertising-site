import django_filters.rest_framework
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializers.BbSerializer import BbSerializer
from .serializers.BbDetailSerializer import BbDetailSerializer
from .serializers.CommentSerializer import CommentSerializer

from main.models import Bb, Comment

class Bbs(generics.ListCreateAPIView):
    queryset = Bb.objects.filter(is_active=True)
    serializer_class = BbSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['author', 'title', 'rubric', 'is_active']

class BbDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Bb.objects.filter(is_active=True)
     serializer_class = BbDetailSerializer

class Comments(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
