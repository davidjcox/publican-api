"""publican_api urls"""

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from publican_api import views

from django.contrib import admin
admin.autodiscover()

# API include patterns
user_patterns = patterns('', 
    url(r'^/$',,), 
    url(r'^/(?P<user_pk>[0-9]+)/$', views.?, name='?'), 
    url(r'^(/(?P<user_slug>\b[a-z0-9\-]+\b)/$', views.?, name='?'), 
)

drink_patterns = patterns('', 
    url(r'^/$',,), 
    url(r'^/(?P<drink_pk>[0-9]+)/$', views.?, name='?'), 
    url(r'^(/(?P<drink_slug>\b[a-z0-9\-]+\b)/$', views.?, name='?'), 
)

facility_patterns = patterns('', 
    url(r'^/$', views.?, name='?'), 
    url(r'^/(?P<facility_pk>[0-9]+)/$', views.?, name='?'), 
    url(r'^(/(?P<facility_slug>\b[a-z0-9\-]+\b)/$', views.?, name='?'), 
)

glass_patterns = patterns('', 
    url(r'^/$', views.?, name='?'), 
    url(r'^/(?P<glass_pk>[0-9]+)/$', views.?, name='?'), 
    url(r'^(/(?P<glass_slug>\b[a-z0-9\-]+\b)/$', views.?, name='?'), 
)

style_patterns = patterns('', 
    url(r'^/$', views.?, name='?'), 
    url(r'^/(?P<style_pk>[0-9]+)/$', views.?, name='?'), 
    url(r'^(/(?P<style_slug>\b[a-z0-9\-]+\b)/$', views.?, name='?'), 
)

review_patterns = patterns('', 
    url(r'^/$', views.?, name='?'), 
    url(r'^/(?P<review_pk>[0-9]+)/$', views.?, name='?'), 
    url(r'^(/(?P<review_slug>\b[a-z0-9\-]+\b)/$', views.?, name='?'), 
)

document_patterns = patterns('', 
    url(r'^/$', views.?, name='?'), 
    url(r'^/(?P<review_pk>[0-9]+)/$', views.?, name='?'), 
    url(r'^(/(?P<review_slug>\b[a-z0-9\-]+\b)/$', views.?, name='?'), 
)

# API endpoints
urlpatterns += format_suffix_patterns(patterns('', 
    url(r'^$', 'api_root'), 
    
    url(r'^users', include(user_patterns)), 
    
    url(r'^(?P<drink>(beer|wine|liquor))', include(drink_patterns)), 
    
    url(r'^(?P<facility>(brewery|winery|distillery))', include(facility_patterns)), 
    url(r'^(?P<drink>(beer|wine|liquor))/(?P<facility>(brewery|winery|distillery))', include(facility_patterns)), 
    url(r'^(?P<drink>(beer|wine|liquor))/(?P<drink_pk>[0-9]+)/(?P<facility>(brewery|winery|distillery))', include(facility_patterns)), 
    url(r'^(?P<drink>(beer|wine|liquor))/(?P<drink_slug>\b[a-z0-9\-]+\b)/(?P<facility>(brewery|winery|distillery))', include(facility_patterns)), 
    
    url(r'^glass', include(glass_patterns)), 
    url(r'^(?P<drink>(beer|wine|liquor))/glass', include(glass_patterns)), 
    url(r'^(?P<drink>(beer|wine|liquor))/(?P<drink_pk>[0-9]+)/glass', include(glass_patterns)), 
    url(r'^(?P<drink>(beer|wine|liquor))/(?P<drink_slug>\b[a-z0-9\-]+\b)/glass', include(glass_patterns)), 
    
    url(r'^style', include(style_patterns)), 
    url(r'^(?P<drink>(beer|wine|liquor))/glass', include(style_patterns)), 
    url(r'^(?P<drink>(beer|wine|liquor))/(?P<drink_pk>[0-9]+)/glass', include(style_patterns)), 
    url(r'^(?P<drink>(beer|wine|liquor))/(?P<drink_slug>\b[a-z0-9\-]+\b)/glass', include(style_patterns)), 
    
    url(r'^review', include(review_patterns)), 
    url(r'^(?P<drink>(beer|wine|liquor))/glass', include(review_patterns)), 
    url(r'^(?P<drink>(beer|wine|liquor))/(?P<drink_pk>[0-9]+)/glass', include(review_patterns)), 
    url(r'^(?P<drink>(beer|wine|liquor))/(?P<drink_slug>\b[a-z0-9\-]+\b)/glass', include(review_patterns)), 
    
    url(r'^(?P<document>(install|execute|require|define|basemodels|models|views|serializers|throttles|permissions))', include(document_patterns)),
))

# Login and logout views for the browsable API
urlpatterns += patterns('', 
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)

# EOF - publican_api urls
