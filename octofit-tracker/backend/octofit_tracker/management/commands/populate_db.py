from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel')
        captain = User.objects.create(email='captain@marvel.com', name='Captain America', team='Marvel')
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='DC')
        superman = User.objects.create(email='superman@dc.com', name='Superman', team='DC')

        # Create activities
        Activity.objects.create(user='Iron Man', activity_type='Running', duration=30)
        Activity.objects.create(user='Captain America', activity_type='Cycling', duration=45)
        Activity.objects.create(user='Batman', activity_type='Swimming', duration=25)
        Activity.objects.create(user='Superman', activity_type='Flying', duration=60)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=85)

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes.')
        Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility.')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
