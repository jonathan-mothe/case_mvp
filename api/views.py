from .serializers import DemandaSerializer
from .models import Demanda
from rest_framework import viewsets, serializers
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly


class DemandaList(viewsets.ModelViewSet):
    queryset = Demanda.objects.all()
    serializer_class = DemandaSerializer
    permission_classes = (IsAuthenticated),
    action_permissions = {
        IsOwnerOrReadOnly: ['update', 'partial_update', 'destroy', 'create'],
        #AllowAny: ['list', 'retrieve']
    }

    def perform_create(self, serializer):
        serializer.save(anunciante=self.request.user)
