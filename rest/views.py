from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .serializers import BoardSerializer
from .models import Board, Cell

class SetBoardViewSet(ModelViewSet):
    serializer_class = BoardSerializer
    
    def get_queryset(self):
        return Board.objects.filter(player=self.request.user.id)
    
    
    def list(self, request, *args, **kwargs):
        instance = self.get_queryset().first()
        if instance is None:
            raise NotFound
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):
        cells = self.request.data['cells']
        for cell in cells:
            Cell(state=cell)
        owner = self.request.user
        serializer.save(player=owner)

