from django.shortcuts import render
from django.http import Http404
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin

from .serializers import BoardSerializer, GameUserRegisterSerializer, GameUserSerializer
from .models import Board, Cell, GameUser

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


class UserRegisterViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    
    def get_serializer_class(self):
        if self.request.method.lower() == 'post':
            return GameUserRegisterSerializer
        elif self.request.method.lower() == 'get':
            return GameUserSerializer
    
    def get_object(self):
        return self.request.user
    

class PlayersListViewSet(ListModelMixin, GenericViewSet):
    serializer_class = GameUserSerializer
    
    def get_queryset(self):
        queryset = GameUser.objects.exclude(id=self.request.user.id)
        return queryset

class UserProfileViewSet(RetrieveModelMixin, GenericViewSet):
    serializer_class = GameUserSerializer
    
    def get_object(self):
        return self.request.user