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
            User.objects.bulk_create([User(**user) for user in data['users']])
            self.stdout.write(self.style.SUCCESS('Users inserted successfully.'))

            self.stdout.write(self.style.WARNING('Inserting Teams...'))
            Team.objects.bulk_create([Team(**team) for team in data['teams']])
            self.stdout.write(self.style.SUCCESS('Teams inserted successfully.'))

            self.stdout.write(self.style.WARNING('Inserting Activities...'))
            Activity.objects.bulk_create([Activity(**activity) for activity in data['activities']])
            self.stdout.write(self.style.SUCCESS('Activities inserted successfully.'))

            self.stdout.write(self.style.WARNING('Inserting Leaderboard...'))
            Leaderboard.objects.bulk_create([Leaderboard(**leaderboard) for leaderboard in data['leaderboard']])
            self.stdout.write(self.style.SUCCESS('Leaderboard inserted successfully.'))

            self.stdout.write(self.style.WARNING('Inserting Workouts...'))
            Workout.objects.bulk_create([Workout(**workout) for workout in data['workouts']])
            self.stdout.write(self.style.SUCCESS('Workouts inserted successfully.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error occurred: {e}'))
