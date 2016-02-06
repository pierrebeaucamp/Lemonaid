from rest_framework import serializers

from apps.scotia.models import Debtor

# Serializers define the API representation.
class DebtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debtor
        fields = ('bank_key',)
