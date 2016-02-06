from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from apps.scotia.urls import router

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'admin/login.html'}, name="my_login"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
