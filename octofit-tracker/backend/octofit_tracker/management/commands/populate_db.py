import json
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data for'

    def handle(self, *args, **kwargs):
        try:
            with open('octofit_tracker/test_data.json') as f:
                data = json.load(f)

            self.stdout.write(self.style.WARNING('Inserting Users...'))
            users = [User(**user) for user in data['users']]
            User.objects.bulk_create(users)
            self.stdout.write(self.style.SUCCESS(f'Users inserted successfully. Count: {len(users)}'))

            self.stdout.write(self.style.WARNING('Inserting Teams...'))
            teams = [Team(**team) for team in data['teams']]
            Team.objects.bulk_create(teams)
            self.stdout.write(self.style.SUCCESS(f'Teams inserted successfully. Count: {len(teams)}'))

            self.stdout.write(self.style.WARNING('Inserting Activities...'))
            activities = [Activity(**activity) for activity in data['activities']]
            Activity.objects.bulk_create(activities)
            self.stdout.write(self.style.SUCCESS(f'Activities inserted successfully. Count: {len(activities)}'))

            self.stdout.write(self.style.WARNING('Inserting Leaderboard...'))
            leaderboards = [Leaderboard(**leaderboard) for leaderboard in data['leaderboard']]
            Leaderboard.objects.bulk_create(leaderboards)
            self.stdout.write(self.style.SUCCESS(f'Leaderboard inserted successfully. Count: {len(leaderboards)}'))

            self.stdout.write(self.style.WARNING('Inserting Workouts...'))
            workouts = [Workout(**workout) for workout in data['workouts']]
            Workout.objects.bulk_create(workouts)
            self.stdout.write(self.style.SUCCESS(f'Workouts inserted successfully. Count: {len(workouts)}'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error occurred: {e}'))
