"""publican_api urls"""

from django.conf.urls import include, patterns, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework_extensions.routers import ExtendedSimpleRouter

import publican_api.basemodels as api_basemodels
import publican_api.views as api_views
import publican_api.utils as api_utils


admin.autodiscover()


urlpatterns = (patterns('', 
    url(r'^$', api_views.PublicanRoot.as_view()),
))

resources_router = SimpleRouter()
resources_router.register(r'beers', api_views.BeerViewSet)
resources_router.register(r'wines', api_views.WineViewSet)
resources_router.register(r'liquors', api_views.LiquorViewSet)
resources_router.register(r'breweries', api_views.BreweryViewSet)
resources_router.register(r'wineries', api_views.WineryViewSet)
resources_router.register(r'distilleries', api_views.DistilleryViewSet)
resources_router.register(r'beerglasses', api_views.BeerGlassViewSet)
resources_router.register(r'wineglasses', api_views.WineGlassViewSet)
resources_router.register(r'liquorglasses', api_views.LiquorGlassViewSet)
resources_router.register(r'beerstyles', api_views.BeerStyleViewSet)
resources_router.register(r'winestyles', api_views.WineStyleViewSet)
resources_router.register(r'liquorstyles', api_views.LiquorStyleViewSet)
urlpatterns += resources_router.urls


reviews_router = SimpleRouter()
reviews_router.register(r'beerreviews', api_views.BeerReviewViewSet)
reviews_router.register(r'winereviews', api_views.WineReviewViewSet)
reviews_router.register(r'liquorreviews', api_views.LiquorReviewViewSet)
urlpatterns += reviews_router.urls


users_router = ExtendedSimpleRouter()
users_routes = users_router.register(r'users', 
                                     api_views.UserViewSet, 
                                     base_name='user')
# users_routes.register(r'favorites',
                      # api_views.FavoriteViewSet,
                      # base_name='users-favorites',
                      # parents_query_lookups=['user_favorite_of'])
users_routes.register(r'beerreviews',
                      api_views.BeerReviewViewSet,
                      base_name='beerreviews',
                      parents_query_lookups=['user_publican_api_beerreview_rater'])
users_routes.register(r'winereviews',
                      api_views.WineReviewViewSet,
                      base_name='winereviews',
                      parents_query_lookups=['publican_api_winereview_rater'])
users_routes.register(r'liquorreviews',
                      api_views.LiquorReviewViewSet,
                      base_name='liquorreviews',
                      parents_query_lookups=['publican_api_liquorreview_rater'])
urlpatterns += users_router.urls


# Login, logout, and admin views for the browsable API
urlpatterns += (patterns('', 
    url(r'^api-authorization/', include('rest_framework.urls',namespace='rest_framework')), 
    url(r'^api-administration/', include(admin.site.urls)), 
))


#EOF - publican_api urls