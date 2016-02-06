from rest_framework import routers
from lemonaid import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'profile', views.UserProfileViewSet, base_name='UserProfiles')
router.register(r'flow', views.FlowViewSet, base_name='Flows')
router.register(r'loan', views.LoanViewSet, base_name='Loans')

