from .models import Board, GameUser, Cell
from rest_framework.serializers import ModelSerializer



class CellSerializer(ModelSerializer):
    class Meta:
        model = Cell
        fields = ['id', 'is_ship', 'is_shooted','coordinate_y','coordinate_x',]


class BoardSerializer(ModelSerializer):
    cells = CellSerializer(many=True, read_only=False)
    class Meta:
        model = Board
        fields = ['id', 'player', 'cells']