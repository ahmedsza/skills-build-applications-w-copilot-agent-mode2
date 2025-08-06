from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    class Meta:
        db_table = "users"

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.JSONField()
    class Meta:
        db_table = "teams"

class Activity(models.Model):
    activity_id = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    class Meta:
        db_table = "activity"

class Leaderboard(models.Model):
    leaderboard_id = models.CharField(max_length=100, unique=True)
    scores = models.JSONField()
    class Meta:
        db_table = "leaderboard"

class Workout(models.Model):
    workout_id = models.CharField(max_length=100, unique=True)
    exercises = models.JSONField()
    class Meta:
        db_table = "workouts"
