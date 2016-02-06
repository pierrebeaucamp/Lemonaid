from rest_framework import routers
from lemonaid import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'profile', views.UserProfileViewSet, base_name='UserProfiles')
router.register(r'cash-flow', views.CashFlowViewSet, base_name='CashFlows')
router.register(r'single-loan', views.SingleLoanViewSet, base_name='SingleLoans')
router.register(r'pool-loan', views.PoolLoanViewSet, base_name='PoolLoans')
router.register(r'pool', views.PoolViewSet, base_name='Pools')
router.register(r'debitor', views.DebitorLoanViewSet, base_name='Debitors')

