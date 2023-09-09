"""publican_api urls"""

from django.conf.urls import include, patterns, url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

import publican_api.basemodels as api_basemodels
import publican_api.views as api_views
import publican_api.utils as api_utils

admin.autodiscover()


# API include patterns
users_favorites_patterns = patterns('', 
    url(r'^(?P<entity>\b[a-z0-9\-]+\b)/(?P<entity_id>\b[a-z0-9\-]+\b)/$', 
        api_views.FavoriteDetail.as_view(), 
        name='favorite_detail'), 
    url(r'^(?P<entity>\b[a-z0-9\-]+\b)/$', 
        api_views.FavoriteList.as_view(), 
        name='favorite_list'), 
    url(r'^$', 
        api_views.FavoriteList.as_view(), 
        name='favorite_list'), 
)

users_reviews_patterns = patterns('', 
    url(r'^(?P<entity>\b[a-z0-9\-]+\b)/(?P<entity_id>\b[a-z0-9\-]+\b)/$', 
        api_views.ReviewDetail.as_view(), 
        name='review_detail'), 
    url(r'^(?P<entity>\b[a-z0-9\-]+\b)/$', 
        api_views.ReviewList.as_view(), 
        name='review_list'), 
    url(r'^$', 
        api_views.ReviewList.as_view(), 
        name='review_list'), 
)

users_patterns = patterns('', 
    url(r'^(?P<user_id>\b[a-z0-9\-]+\b)/favorites/', 
        include(users_favorites_patterns)), 
    url(r'^(?P<user_id>\b[a-z0-9\-]+\b)/reviews/', 
        include(users_reviews_patterns)), 
    url(r'^(?P<user_id>\b[a-z0-9\-]+\b)/$', 
        api_views.UserRetrieveUpdateDestroy.as_view(), 
        name='user_retrieve_update_destroy'), 
    url(r'^$',
        api_views.UserListCreate.as_view(), 
        name='user_list_create',), 
)

drinks_patterns = patterns('', 
    url(r'^(?P<drink_id>\b[a-z0-9\-]+\b)/$', 
        api_views.DrinkRetrieveUpdateDestroyView.as_view(), 
        name='drink_retrieve_update_destroy'), 
    url(r'^$', 
        api_views.DrinkListCreateView.as_view(), 
        name='drink_list_create'), 
)

facilities_patterns = patterns('', 
    url(r'^(?P<facility_id>\b[a-z0-9\-]+\b)/$', 
        api_views.FacilityRetrieveUpdateDestroyView.as_view(), 
        name='facility_retrieve_update_destroy'), 
    url(r'^$', 
        api_views.FacilityListCreateView.as_view(), 
        name='facility_list_create'), 
)

glasses_patterns = patterns('', 
    url(r'^(?P<glass_id>\b[a-z0-9\-]+\b)/$', 
        api_views.GlassRetrieveUpdateDestroyView.as_view(), 
        name='glass_retrieve_update_destroy'), 
    url(r'^$', 
        api_views.GlassListCreateView.as_view(), 
        name='glass_list_create'), 
)

styles_patterns = patterns('', 
    url(r'^(?P<style_id>\b[a-z0-9\-]+\b)/$', 
        api_views.StyleRetrieveUpdateDestroyView.as_view(), 
        name='style_retrieve_update_destroy'), 
    url(r'^$', 
        api_views.StyleListCreateView.as_view(), 
        name='style_list_create'), 
)

reviews_patterns = patterns('', 
    url(r'^(?P<review_id>\b[a-z0-9\-]+\b)/$', 
        api_views.ReviewRetrieveUpdateDestroyView.as_view(), 
        name='review_retrieve_update_destroy'), 
    url(r'^$', 
        api_views.ReviewListCreateView.as_view(), 
        name='review_list_create'), 
)

documents_patterns = patterns('', 
    url(r'^(?P<document_id>\b[a-z0-9\-]+\b)/$', 
        api_views.DocumentRetrieveView.as_view(), 
        name='document_retrieve_update_destroy'), 
    url(r'^$', 
        api_views.DocumentListView.as_view(), 
        name='document_list_create'), 
)


# API literal model name regexes
drink_regex = api_utils.get_entity_regex(api_basemodels.Drink)
facility_regex = api_utils.get_entity_regex(api_basemodels.Facility)
glass_regex = api_utils.get_entity_regex(api_basemodels.Glass)
style_regex = api_utils.get_entity_regex(api_basemodels.Style)
review_regex = api_utils.get_entity_regex(api_basemodels.Review)
document_regex = api_utils.get_entity_regex(api_basemodels.Document)


# API endpoints
urlpatterns = (patterns('', 
    url(r'^users/', include(users_patterns)), 
    url(drink_regex, include(drinks_patterns)), 
    url(facility_regex, include(facilities_patterns)), 
    url(glass_regex, include(glasses_patterns)), 
    url(style_regex, include(styles_patterns)), 
    url(review_regex, include(reviews_patterns)), 
    url(document_regex, include(documents_patterns)),
))

# Login and logout views for the browsable API
urlpatterns += (patterns('', 
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
))


# EOF - publican_api urls
