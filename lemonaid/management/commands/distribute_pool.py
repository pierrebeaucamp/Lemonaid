from django.core.management.base import BaseCommand, CommandError

from lemonaid.serializers import UserProfileNoHyperlinkSerializer
from lemonaid.models import UserProfile

class Command(BaseCommand):
    help = 'Distributes the pool to the people'

    def handle(self, *args, **options):
        if UserProfile.objects.all().count() == 0:
            raise CommandError('UserProfiles does not exist')

        profiles = UserProfile.objects.all()

        serializer = UserProfileNoHyperlinkSerializer(profiles, many=True)

        self.stdout.write(self.style.SUCCESS('profiles = {}'.format(serializer.data )))