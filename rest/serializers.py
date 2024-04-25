from .models import Board, GameUser, Cell
from rest_framework.serializers import ModelSerializer


class CellSerializer(ModelSerializer):
    class Meta:
        model = Cell
        fields = ['id', 'state', 'coordinate_y','coordinate_x']


class BoardSerializer(ModelSerializer):
    cells = CellSerializer(many=True, read_only=False)
    class Meta:
        model = Board
        fields = ['id', 'player', 'cells']
        read_only_fields = ['player']
        
    def create(self, validated_data):
        cells = validated_data.pop('cells')
        board, _ = Board.objects.get_or_create(**validated_data)
        
        for cell in cells:
            state = cell.pop('state')
            Cell.objects.update_or_create(board=board, **cell, defaults={"state": state})
        return board
        
        
class GameUserRegisterSerializer(ModelSerializer):
    class Meta:
        model = GameUser
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'style': {'input_type': 'password'}}}

        
    def create(self, validated_data):
        return GameUser.objects.create_user(**validated_data)
    
    
class GameUserSerializer(ModelSerializer):
    class Meta:
        model = GameUser
        fields = ['id', 'username']