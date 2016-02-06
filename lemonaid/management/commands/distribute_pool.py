from django.core.management.base import BaseCommand, CommandError

from lemonaid.serializers import PoolLoanSerializer
from lemonaid.models import UserProfile, PoolLoan, Pool

class Command(BaseCommand):
    help = 'Distributes the pool to the people'

    def handle(self, *args, **options):
        if UserProfile.objects.all().count() == 0:
            raise CommandError('UserProfiles does not exist')


        pools = Pool.objects.all()

        to_distribute = []
        for pool in pools:
            to_distribute = PoolLoan.objects.filter(interest=pool.interest_rate)
            distribute_amt = pool.amount / to_distribute.count()
            # for loan in to_distribute:
            #     to_distribute.profile



        serializer = PoolLoanSerializer(to_distribute, many=True)

        self.stdout.write(self.style.SUCCESS('to_distribute pool_loans = {}'.format(serializer.data)))