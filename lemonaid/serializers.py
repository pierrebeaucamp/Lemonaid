from rest_framework import serializers

from django.contrib.auth.models import User, Group

from lemonaid.models import UserProfile


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

    class Meta:
        model = UserProfile
        fields = ('bank_key', 'title', 'date_of_birth', 'marital_status', 'sin',
                  'address', 'city', 'province', 'postal_code', 'residential_status',
                  'user',)
