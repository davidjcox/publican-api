"""publican_api urls"""

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from publican_api import views

from django.contrib import admin
admin.autodiscover()


# API endpoints
urlpatterns += format_suffix_patterns(patterns('', 
    url(r'^$', 'api_root'), 
    url(r'^users/$', 
        views.UserList.as_view()), 
    url(r'^users/(?P<pk>[0-9]+)/$', 
        views.UserDetail.as_view()), 
    url(r'^(?P<drink>(beer|wine|liquor))/', 
        views.DrinkListView.as_view(), 
        name='drink-GET'), 
    url(r'^(?P<drink>(beer|wine|liquor))/', include(patterns('', 
        url(r'^(?P<pk>[0-9]+)/$', 
            views.DrinkRetrieveUpdateDestroyView.as_view(), 
            name='drink_pk-GET_POST_DEST'), 
        url(r'^(?P<slug>\b[a-z0-9\-]+\b)/$', 
            views.DrinkRetrieveUpdateDestroyView.as_view(), 
            name='drink_slug-GET_POST_DEST'), 
        url(r'^(brewery|winery|distillery)/$', 
            views.FacilityListView.as_view(), 
            name='facility-GET'), 
        url(r'^(brewery|winery|distillery)/(?P<pk>[0-9]+)/$', 
            views.FacilityRetrieveUpdateDestroyView.as_view(), 
            name='facility_pk-GET_POST_DEST'), 
        url(r'^(brewery|winery|distillery)/(?P<slug>\b[a-z0-9\-]+\b)/$', 
            views.FacilityRetrieveUpdateDestroyView.as_view(), 
            name='facility_slug-GET_POST_DEST'), 
        url(r'^glass/$', 
            views.GlassListView.as_view(), 
            name='glass-GET'), 
        url(r'^glass/(?P<pk>[0-9]+)/$', 
            views.GlassRetrieveUpdateDestroyView.as_view(), 
            name='glass_pk-GET_POST_DEST'), 
        url(r'^glass/(?P<slug>\b[a-z0-9\-]+\b)/$', 
            views.GlassRetrieveUpdateDestroyView.as_view(), 
            name='glass_slug-GET_POST_DEST'), 
        url(r'^style/$', 
            views.StyleListView.as_view(), 
            name='style-GET'), 
        url(r'^style/(?P<pk>[0-9]+)/$', 
            views.StyleRetrieveUpdateDestroyView.as_view(), 
            name='style_pk-GET_POST_DEST'), 
        url(r'^style/(?P<slug>\b[a-z0-9\-]+\b)/$', 
            views.StyleRetrieveUpdateDestroyView.as_view(), 
            name='style_slug-GET_POST_DEST'), 
        url(r'^review/$', 
            views.ReviewListView.as_view(), 
            name='review-GET'), 
        url(r'^review/(?P<pk>[0-9]+)/$', 
            views.ReviewRetrieveUpdateDestroyView.as_view(), 
            name='review_pk-GET_POST_DEST'), 
        url(r'^review/(?P<slug>\b[a-z0-9\-]+\b)/$', 
            views.ReviewRetrieveUpdateDestroyView.as_view(), 
            name='review_slug-GET_POST_DEST'), 
    ))), 
    url(r'^(?P<document>(install|execute|require|define|basemodels|models|views|serializers|throttles|permissions))/',
        include(patterns('', 
        url(r'^(?P<pk>[0-9]+)/$', 
            views.DocumentRetrieveView.as_view(), 
            name='document_pk-GET'), 
        url(r'^(?P<slug>\b[a-z0-9\-]+\b)/$', 
            views.DocumentRetrieveView.as_view(), 
            name='document_slug-GET'), 
    ))), 
))


# Login and logout views for the browsable API
urlpatterns += patterns('', 
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)

# EOF - publican_api urls