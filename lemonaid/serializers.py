from django.db.models import Sum, F
from rest_framework import serializers

from django.contrib.auth.models import User, Group

from lemonaid.models import UserProfile, CashFlow, SingleLoan, PoolLoan, Pool, DebitorLoan


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


# Serializers define the API representation.
class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', queryset=User.objects.all())
    single_loan_total = serializers.SerializerMethodField(read_only=True)

    def get_single_loan_total(self, obj):
        return obj.get_single_loan_total()

    class Meta:
        model = UserProfile
        fields = ('bank_key', 'title', 'date_of_birth', 'marital_status', 'sin',
                  'address', 'city', 'province', 'postal_code', 'residential_status', 'type',
                  'user', 'single_loan_total',)

# Serializers define the API representation.
class UserProfileNoHyperlinkSerializer(serializers.ModelSerializer):
    single_loan_total = serializers.SerializerMethodField(read_only=True)

    def get_single_loan_total(self, obj):
        return obj.get_single_loan_total()

    class Meta:
        model = UserProfile
        fields = ('bank_key', 'title', 'date_of_birth', 'marital_status', 'sin',
                  'address', 'city', 'province', 'postal_code', 'residential_status', 'type',
                  'single_loan_total')


# Serializers define the API representation.
class CashFlowSerializer(serializers.ModelSerializer):
    profile = serializers.HyperlinkedRelatedField(view_name='UserProfiles-detail', queryset=UserProfile.objects.all())

    class Meta:
        model = CashFlow
        fields = ('profile', 'name', 'flow_type', 'duration_type', 'amount', 'date',)


class DebitorLoanSerializer(serializers.ModelSerializer):
    debitor = serializers.HyperlinkedRelatedField(view_name='UserProfiles-detail', queryset=UserProfile.objects.filter(type='d'))

    class Meta:
        model = DebitorLoan
        fields = ('debitor', 'amount',)


# Serializers define the API representation.
class SingleLoanSerializer(serializers.ModelSerializer):
    creditor = serializers.HyperlinkedRelatedField(view_name='UserProfiles-detail', queryset=UserProfile.objects.filter(type='c'))
    debitor = serializers.HyperlinkedRelatedField(view_name='UserProfiles-detail', queryset=UserProfile.objects.filter(type='d'))

    class Meta:
        model = SingleLoan
        fields = ('creditor', 'debitor', 'amount', 'interest', 'duration',)


# Serializers define the API representation.
class PoolLoanSerializer(serializers.ModelSerializer):
    creditor = serializers.HyperlinkedRelatedField(many=True, view_name='UserProfiles-detail', queryset=UserProfile.objects.filter(type='c'))

    class Meta:
        model = PoolLoan
        fields = ('creditor', 'amount', 'interest', 'duration',)



# Serializers define the API representation.
class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pool
        fields = ('type', 'interest_rate', 'amount',)

