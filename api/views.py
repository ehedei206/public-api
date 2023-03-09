from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from api.serializers import UserSerializer, BoardSerializer, ColumnSerializer, TicketSerializer, DetailedBoardSerializer
from api.models import Board, Column, Ticket
from api.permissions import BoardPermission, ColumnPermission, TicketPermission
from api.pagination import SmallResultsSetPagination

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated & BoardPermission]
    pagination_class = SmallResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    def get_serializer_class(self):
        if self.detail == True:
            return DetailedBoardSerializer
        
        else:
            return BoardSerializer

class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = [permissions.IsAuthenticated & ColumnPermission]

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated & TicketPermission]

class SelfViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BoardSerializer

    def get_queryset(self):
        user = self.request.user
        return Board.objects.filter(users__id=user.id)

