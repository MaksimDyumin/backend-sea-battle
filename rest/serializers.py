from .models import Board, GameUser, Cell, Ship
from rest_framework.serializers import ModelSerializer


class CellSerializer(ModelSerializer):
    class Meta:
        model = Cell
        fields = ['id', 'state', 'coordinate_y','coordinate_x']


class ShipSerializer(ModelSerializer):
    cells = CellSerializer(many=True, read_only=False)
    class Meta:
        model = Ship
        fields = ['id', 'board', 'cells']
        read_only_fields = ['board']


class BoardSerializer(ModelSerializer):
    cells = CellSerializer(many=True, read_only=False)
    ships = ShipSerializer(many=True, read_only=False)
    class Meta:
        model = Board
        fields = ['id', 'player', 'cells', 'ships']
        read_only_fields = ['player']
        
    def create(self, validated_data):
        cells = validated_data.pop('cells')
        ships = validated_data.pop('ships')
        board, _ = Board.objects.get_or_create(**validated_data)
        
        for cell in cells:
            state = cell.pop('state')
            Cell.objects.update_or_create(board=board, **cell, defaults={"state": state})
            
        for ship in ships:
            ship_cells = ship.pop('cells')
            ship_obj = Ship.objects.create(board=board)
            cell_obj_list = []
            for ship_cell in ship_cells:
                ship_cell_state = ship_cell.pop('state')
                cell_obj, _ = Cell.objects.update_or_create(board=board, ship=ship_obj, **ship_cell, defaults={"state": ship_cell_state, "ship": ship_obj})
                cell_obj_list.append(cell_obj)
                
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