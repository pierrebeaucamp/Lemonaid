from rest_framework import viewsets

from lemonaid.models import Debtor
from lemonaid.serializers import DebtorSerializer

# ViewSets define the view behavior.
class DebtorViewSet(viewsets.ModelViewSet):
    queryset = Debtor.objects.all()
    serializer_class = DebtorSerializer
