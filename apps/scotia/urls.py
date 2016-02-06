
from rest_framework import routers
from apps.scotia import views


router = routers.DefaultRouter()
router.register(r'debtor', views.DebtorViewSet, base_name='Debtors')

