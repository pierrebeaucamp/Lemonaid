from rest_framework import viewsets

from django.contrib.auth.models import User, Group

from lemonaid.models import UserProfile, CashFlow, SingleLoan, PoolLoan, Pool, DebitorLoan
from lemonaid.serializers import UserProfileSerializer, UserSerializer, GroupSerializer, CashFlowSerializer, SingleLoanSerializer, PoolLoanSerializer, PoolSerializer, DebitorLoanSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# ViewSets define the view behavior.
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


# ViewSets define the view behavior.
class CashFlowViewSet(viewsets.ModelViewSet):
    queryset = CashFlow.objects.all()
    serializer_class = CashFlowSerializer


# ViewSets define the view behavior.
class SingleLoanViewSet(viewsets.ModelViewSet):
    queryset = SingleLoan.objects.all()
    serializer_class = SingleLoanSerializer


# ViewSets define the view behavior.
class PoolLoanViewSet(viewsets.ModelViewSet):
    queryset = PoolLoan.objects.all()
    serializer_class = PoolLoanSerializer

    # create
    # list
    # retrieve
    # delete
    #


class PoolViewSet(viewsets.ModelViewSet):
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer


class DebitorLoanViewSet(viewsets.ModelViewSet):
    queryset = DebitorLoan.objects.all()
    serializer_class = DebitorLoanSerializer