from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Board, Column, Ticket

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ['url', 'name', 'users']

    def validate(self, data):
        if self.context['request'].method == 'POST':
            if 'users' in data:
                if not self.context['request'].user in data['users']:
                    raise serializers.ValidationError(
                        {'users': 'must add yourself as user to new boards'}
                    )
            else:
                raise serializers.ValidationError(
                    {'users': 'you must provide a list of users for new boards'}
                )
        return super().validate(data)

class ColumnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Column
        fields = ['url', 'name', 'board']

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ['url', 'name', 'description', 'column']

class DetailedColumnSerializer(serializers.HyperlinkedModelSerializer):
    tickets = TicketSerializer(source="ticket_set", read_only=True, many=True)
    class Meta:
        model = Column
        fields = ['url', 'name', 'board', 'tickets']

class DetailedBoardSerializer(serializers.HyperlinkedModelSerializer):
    columns = DetailedColumnSerializer(source="column_set", read_only=True, many=True)
    class Meta:
        model = Board
        fields = ['url', 'name', 'users', 'columns']