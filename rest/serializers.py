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
        
    