"""drf_exts profiling urls"""

from rest_framework_extensions.routers import ExtendedSimpleRouter
from drf_exts.views import DrinkViewSet, GlassViewSet

import pdb; pdb.Pdb().set_trace()

router = ExtendedSimpleRouter()
(
    router.register(r'drinks', 
                    DrinkViewSet, 
                    base_name='drink')
          .register(r'glasses',
                    GlassViewSet,
                    base_name='drinks-glasses',
                    parents_query_lookups=['drink_glasses'])
)
urlpatterns = router.urls


# EOF