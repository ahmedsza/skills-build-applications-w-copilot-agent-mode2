from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25)
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Team A", members=["User1", "User2"])
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        activity = Activity.objects.create(activity_id="A1", type="Running", duration=30)
        self.assertEqual(activity.type, "Running")

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(leaderboard_id="L1", scores={"User1": 100})
        self.assertEqual(leaderboard.scores["User1"], 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(workout_id="W1", exercises=["Push-ups", "Squats"])
        self.assertEqual(workout.workout_id, "W1")
