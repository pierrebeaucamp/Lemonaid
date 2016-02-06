from rest_framework import viewsets

from apps.scotia.models import Debtor
from apps.scotia.serializers import DebtorSerializer

# Create your views here.

# ViewSets define the view behavior.
class DebtorViewSet(viewsets.ModelViewSet):
    queryset = Debtor.objects.all()
    serializer_class = DebtorSerializer
