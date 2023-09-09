

from rest_framework_extensions.routers import ExtendedSimplerouter

from publican_api import models as api_models


nested_router = ExtendedSimpleRouter()
(
    nested_router.register(r'users', 
                           UserViewSet, 
                           base_name='user')
                 .register(r'reviews', 
                           ReviewViewSet, 
                           base_name='users_review', 
                           parents_query_lookups=['review__rater'])
                 .register(r'(?P<entity>\b[a-z0-9\-]+\b)', 
                           FavoriteViewSet, 
                           base_name='review_entity',
                           parents_query_lookups=['favorite_of__user'])