from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout
from bson import ObjectId

class StringObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)
    def to_internal_value(self, data):
        return ObjectId(data)

class UserSerializer(serializers.ModelSerializer):
    id = StringObjectIdField(source='_id', read_only=True)
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class TeamSerializer(serializers.ModelSerializer):
    id = StringObjectIdField(source='_id', read_only=True)
    class Meta:
        model = Team
        fields = ['id', 'name']

class ActivitySerializer(serializers.ModelSerializer):
    id = StringObjectIdField(source='_id', read_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'type', 'duration']

class LeaderboardSerializer(serializers.ModelSerializer):
    id = StringObjectIdField(source='_id', read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'points']

class WorkoutSerializer(serializers.ModelSerializer):
    id = StringObjectIdField(source='_id', read_only=True)
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description']
