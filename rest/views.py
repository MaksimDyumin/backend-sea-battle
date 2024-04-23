from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import BoardSerializer
from .models import Board

class SetBoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    
    def get_queryset(self):
        return Board.objects.filter(player=self.request.user.id)
    # def get_queryset(self):
    #     pass

