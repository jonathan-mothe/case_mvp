from .serializers import DemandaSerializer
from .models import Demanda
from rest_framework import viewsets, serializers
from django.shortcuts import render


class DemandaList(viewsets.ModelViewSet):
    queryset = Demanda.objects.all()
    serializer_class = DemandaSerializer

    def perform_create(self, serializer):
        serializer.save(anunciante=self.request.user)