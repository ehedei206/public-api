from api.models import Board, Column
from rest_framework.permissions import BasePermission, SAFE_METHODS


class BoardPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        if obj.users.filter(id=request.user.id).exists():
            return True
        
        return False
    

class ColumnPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        if obj.board.users.filter(id=request.user.id).exists():
            return True
        
        return False
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if "board" in request.data:
            board_id = parse_id_from_url(request.data["board"])
            board = Board.objects.get(id=board_id)

            if board.users.filter(id=request.user.id).exists():
                return True
            else:
                return False
            
        return True

class TicketPermission(BasePermission):
    def has_object_permissions(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        if obj.column.board.users.filter(id=request.user.id).exists():
            return True
        return False
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        if "column" in request.data:
            column_id = parse_id_from_url(request.data["column"])
            column = Column.objects.get(id=column_id)

            board = column.board

            if board.users.filter(id=request.user.id).exists():
                return True
            else:
                return False
        return True
            

def parse_id_from_url(url):
    split_url = url.removesuffix("/").split("/")
    if len(split_url) < 1:
        return None
    
    id = split_url[-1]
    if not id.isdigit():
        return None
    
    return id