"""drf-nested_api profiling urls"""

from drf_nested.views import DrinkViewSet, GlassViewSet

from rest_framework_nested import routers

from django.conf.urls import patterns, url, include


drinks_router = routers.SimpleRouter()
drinks_router.register(r'drinks', DrinkViewSet)

glasses_router = routers.SimpleRouter()
glasses_router.register(r'glasses', GlassViewSet)

import pdb; pdb.Pdb().set_trace()

glasses_nested_router = routers.NestedSimpleRouter(drinks_router, r'drinks', lookup='drink')
glasses_nested_router.register(r'glasses', GlassViewSet)

urlpatterns = patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(drinks_router.urls)),
    url(r'^', include(glasses_router.urls)),
    url(r'^', include(glasses_nested_router.urls)),
)


# EOF