from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = patterns('',
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)


url(r'^users/$', views.UserList.as_view()),
url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),


urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)

urlpatterns = patterns('',
    url(r'^(?P<page_slug>\w+)-(?P<page_id>\w+)/', include(patterns('wiki.views',
        url(r'^history/$', 'history'),
        url(r'^edit/$', 'edit'),
        url(r'^discuss/$', 'discuss'),
        url(r'^permissions/$', 'permissions'),
    ))),
)

urlpatterns = format_suffix_patterns(patterns('', 
    url(r'^(?P<drink>(beer|wine|liquor))/', include(patterns('', 
        url(r'^(?P<pk>[0-9]+)/$'), 
        url(r'^(?P<slug>\b[a-z0-9\-]+\b)/$'), 
        url(r'^(brewery|winery|distillery)/$'), 
        url(r'^(brewery|winery|distillery)/(?P<pk>[0-9]+)/$'), 
        url(r'^(brewery|winery|distillery)/(?P<slug>\b[a-z0-9\-]+\b)/$'), 
        url(r'^glass/$'), 
        url(r'^glass/(?P<pk>[0-9]+)/$'), 
        url(r'^glass/(?P<slug>\b[a-z0-9\-]+\b)/$'), 
        url(r'^style/$'), 
        url(r'^style/(?P<pk>[0-9]+)/$'), 
        url(r'^style/(?P<slug>\b[a-z0-9\-]+\b)/$'), 
        url(r'^review/$'), 
        url(r'^review/(?P<pk>[0-9]+)/$'), 
        url(r'^review/(?P<slug>\b[a-z0-9\-]+\b)/$'), 
    ))), 
))
    
# API endpoints
urlpatterns = format_suffix_patterns(patterns('snippets.views',
    url(r'^$', 'api_root'),
    url(r'^snippets/$',
        views.SnippetList.as_view(),
        name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail')
))

# Login and logout views for the browsable API
urlpatterns += patterns('',    
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)