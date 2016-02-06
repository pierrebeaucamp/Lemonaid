from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from lemonaid.urls import router

urlpatterns = [
    url(r'^api/', include(router.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'admin/login.html'}, name="my_login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name="my_logout"),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
