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
    pool = serializers.SerializerMethodField()

    def get_pool(self, obj):
        return obj.dgddfhgdkjf()

    class Meta:
        model = UserProfile
        fields = ('bank_key', 'title', 'date_of_birth', 'marital_status', 'sin',
                  'address', 'city', 'province', 'postal_code', 'residential_status', 'type',
                  'user', 'pool',)

# Serializers define the API representation.
class UserProfileNoHyperlinkSerializer(serializers.ModelSerializer):
    pool = serializers.SerializerMethodField()

    def get_pool(self, obj):
        return obj.dgddfhgdkjf()

    class Meta:
        model = UserProfile
        fields = ('bank_key', 'title', 'date_of_birth', 'marital_status', 'sin',
                  'address', 'city', 'province', 'postal_code', 'residential_status', 'type',
                  'pool',)



# Serializers define the API representation.
class CashFlowSerializer(serializers.ModelSerializer):
    profile = serializers.HyperlinkedRelatedField(view_name='UserProfiles-detail', queryset=UserProfile.objects.all())

    class Meta:
        model = CashFlow
        fields = ('profile', 'name', 'flow_type', 'duration_type', 'amount', 'date',)


# Serializers define the API representation.
class SingleLoanSerializer(serializers.ModelSerializer):
    profile = serializers.HyperlinkedRelatedField(view_name='UserProfiles-detail', queryset=UserProfile.objects.all())

    class Meta:
        model = SingleLoan
        fields = ('profile', 'amount', 'interest', 'duration',)


# Serializers define the API representation.
class PoolLoanSerializer(serializers.ModelSerializer):
    profile = serializers.HyperlinkedRelatedField(view_name='UserProfiles-detail', queryset=UserProfile.objects.all())

    class Meta:
        model = PoolLoan
        fields = ('profile', 'amount', 'interest', 'duration',)


# Serializers define the API representation.
class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pool
        fields = ('type', 'interest_rate', 'amount',)


# Serializers define the API representation.
class DebitorLoanSerializer(serializers.ModelSerializer):
    profile = serializers.HyperlinkedRelatedField(view_name='UserProfiles-detail', queryset=UserProfile.objects.all())

    class Meta:
        model = DebitorLoan
        fields = ('profile', 'single_loan', 'pool_loan',)
