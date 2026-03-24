from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Team, Activity, Leaderboard, Workout
from django.contrib.auth import get_user_model

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.team = Team.objects.create(name='Test Team')
        self.activity = Activity.objects.create(user='testuser', type='run', duration=10)
        self.leaderboard = Leaderboard.objects.create(user='testuser', points=50)
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc')

    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_team_list(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_activity_list(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leaderboard_list(self):
        response = self.client.get('/api/leaderboards/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_workout_list(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
