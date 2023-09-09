"""publican_api views"""

from collections import OrderedDict

from django.db import models
from django.db.models import Q
from django.http import Http404
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import NoReverseMatch
from django.contrib.contenttypes.models import ContentType

from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import generics

from rest_framework_extensions.mixins import NestedViewSetMixin

import publican_api.models as api_models
import publican_api.basemodels as api_basemodels
import publican_api.serializers as api_serializers
import publican_api.permissions as api_permissions
import publican_api.throttles as api_throttles


def get_subclassed_models(_app_label, _app_mod, _base_model):
    return [models.get_model(app_label=_app_label, model_name=_model.__name__) 
                for _model in models.get_models(app_mod=_app_mod) 
                if issubclass(_model, _base_model)]
# /get_subclassed_models


def get_instance(_models, _clue):
    if isinstance(_clue, str):
        for _model in _models:
            try:
              return _model.objects.get(Q(name=_clue) | Q(slug=_clue))
            except _model.DoesNotExist:
              continue #Ignore any model that doesn't return a result during loop.
        raise Http404 #But, if no model returned a query result, raise not found.
    raise ParseError("Attribute to search must be 'name' or 'slug' of item.")
# /get_instance


def custom_exception_handler(exc):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    return response
# /custom_exception_handler


class PublicanRoot(APIView):
    """
    <pre>
    Finds all publican entities and returns them as hyperlinked resources.
    </pre>
    """
    def get(self, request, *args, **kwargs):
        _app_label = settings.APP_LABEL
        _models_dict = OrderedDict()
        
        _resource_models = get_subclassed_models(_app_label, 
                                                 api_models, 
                                                 api_basemodels.Resource)
        
        _review_models = get_subclassed_models(_app_label, 
                                               api_models, 
                                               api_basemodels.Review)
        
        
        #Add users to first position in sorted root dictionary.
        _models_dict['users'] = reverse('user-list', 
                                        request=request, 
                                        format=kwargs.get('format', None)
                                        )
        
        #Add favorites to second position in sorted root dictionary.
        # _models_dict['favorites'] = reverse('favorite-list', 
                                        # request=request, 
                                        # format=kwargs.get('format', None)
                                        # )
                
        #Add resources (subclasses of basemodels.Resource) to root dictionary.
        for _rsc_model in _resource_models:
            _model_name = _rsc_model._meta.verbose_name_plural.replace(' ', '')
            _view_name = _rsc_model._meta.verbose_name.replace(' ', '') + "-list"
            _resource_url = reverse(_view_name, 
                                    request=request, 
                                    format=kwargs.get('format', None)
                                    )
            _models_dict[_model_name] = _resource_url
        
        #Add reviews (subclasses of basemodels.Review) to root dictionary.
        for _rvw_model in _review_models:
            _model_name = _rvw_model._meta.verbose_name_plural.replace(' ', '')
            _view_name = _rvw_model._meta.verbose_name.replace(' ', '') + "-list"
            _resource_url = reverse(_view_name, 
                                    request=request, 
                                    format=kwargs.get('format', None)
                                    )
            _models_dict[_model_name] = _resource_url
        
        return Response(_models_dict)
# /PublicanRoot


class BeerViewSet(viewsets.ModelViewSet):
    """
    <pre>
    Handles `beer` resources.
    
    ATTRIBUTES:
    'name':                 (str,       8-128 chars)
    'ibu':                  (int,       5-100)
    'calories':             (int,       50-1000)
    'abv':                  (float,     0-80)
    
    PERMISSIONS:
    authenticated:          (CREATE/RETRIEVE/UPDATE/DELETE)
    anonymous:              (RETRIEVE only)
    
    THROTTLES:
    create:                 (1/day)
    </pre>
    """
    serializer_class = api_serializers.BeerSerializer
    queryset = api_models.Beer.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_classes = (api_throttles.CustomListCreateThrottle,)
    throttle_scope = 'drinkcreate'
# /BeerViewSet


class WineViewSet(viewsets.ModelViewSet):
    """
    <pre>
    Handles `wine` resources.
    
    ATTRIBUTES:
    'name':                 (str,       8-128 chars)
    'sweetness':            (int,       1-1000)
    'acidity':              (float,     0.1-1.0)
    'tannin':               (choice,    'L','H')
    'fruit':                (str,       0-128 chars)
    
    PERMISSIONS:
    authenticated:          (CREATE/RETRIEVE/UPDATE/DELETE)
    anonymous:              (RETRIEVE only)
    
    THROTTLES:
    create:                 (1/day)
    </pre>
    """
    serializer_class = api_serializers.WineSerializer
    queryset = api_models.Wine.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_classes = (api_throttles.CustomListCreateThrottle,)
    throttle_scope = 'drinkcreate'
# /WineViewSet


class LiquorViewSet(viewsets.ModelViewSet):
    """
    <pre>
    Handles `liquor` resources.
    
    ATTRIBUTES:
    'name':                 (str,       8-128 chars)
    'calories':             (int,       50-1000)
    'abv':                  (float,     0-80)
    
    PERMISSIONS:
    authenticated:          (CREATE/RETRIEVE/UPDATE/DELETE)
    anonymous:              (RETRIEVE only)
    
    THROTTLES:
    create:                 (1/day)
    </pre>
    """
    serializer_class = api_serializers.LiquorSerializer
    queryset = api_models.Liquor.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_classes = (api_throttles.CustomListCreateThrottle,)
    throttle_scope = 'drinkcreate'
# /LiquorViewSet


class BreweryViewSet(viewsets.ModelViewSet):
    """
    <pre>
    Handles `brewery` resources.
    
    ATTRIBUTES:
    'name':                 (str,       8-128 chars)
    'location':             (str,       8-128 chars)
    'beer':                 (int,       fk-->Beer<pk>)
    
    PERMISSIONS:
    authenticated:          (CREATE/RETRIEVE/UPDATE/DELETE)
    anonymous:              (RETRIEVE only)
    
    THROTTLES:
    create:                 (1/day)
    </pre>
    """
    serializer_class = api_serializers.BrewerySerializer
    queryset = api_models.Brewery.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_classes = (api_throttles.CustomListCreateThrottle,)
    throttle_scope = 'facilitycreate'
# /BreweryViewSet


class WineryViewSet(viewsets.ModelViewSet):
    """
    <pre>
    Handles `winery` resources.
    
    ATTRIBUTES:
    'name':                 (str,       8-128 chars)
    'location':             (str,       8-128 chars)
    'wine':                 (int,       fk-->Wine<pk>)
    
    PERMISSIONS:
    authenticated:          (CREATE/RETRIEVE/UPDATE/DELETE)
    anonymous:              (RETRIEVE only)
    
    THROTTLES:
    create:                 (1/day)
    </pre>
    """
    serializer_class = api_serializers.WinerySerializer
    queryset = api_models.Winery.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_classes = (api_throttles.CustomListCreateThrottle,)
    throttle_scope = 'facilitycreate'
# /WineryViewSet


class DistilleryViewSet(viewsets.ModelViewSet):
    """
    <pre>
    Handles `distillery` resources.
    
    ATTRIBUTES:
    'name':                 (str,       8-128 chars)
    'location':             (str,       8-128 chars)
    'liquor':               (int,       fk-->Liquor<pk>)
    
    PERMISSIONS:
    authenticated:          (CREATE/RETRIEVE/UPDATE/DELETE)
    anonymous:              (RETRIEVE only)
    
    THROTTLES:
    create:                 (1/day)
    </pre>
    """
    serializer_class = api_serializers.DistillerySerializer
    queryset = api_models.Distillery.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_classes = (api_throttles.CustomListCreateThrottle,)
    throttle_scope = 'facilitycreate'
# /DistilleryViewSet


class BeerGlassViewSet(viewsets.ModelViewSet):
    """
    <pre>
    Handles `beer glass` resources.
    
    ATTRIBUTES:
    'name':                 (str,       8-128 chars)
    'type':                 (str,       8-128 chars)
    'beer':                 (int,       fk-->Beer<pk>)
    
    PERMISSIONS:
    authenticated:          (CREATE/RETRIEVE/UPDATE/DELETE)
    anonymous:              (RETRIEVE only)
    
    THROTTLES:
    create:                 (1/hour)
    </pre>
    """
    serializer_class = api_serializers.BeerGlassSerializer
    queryset = api_models.BeerGlass.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_classes = (api_throttles.CustomListCreateThrottle,)
    throttle_scope = 'glasscreate'
# /BeerGlassViewSet


class WineGlassViewSet(viewsets.ModelViewSet):
    """
    <pre>
    Handles `wine glass` resources.
    
    ATTRIBUTES:
    'name':                 (str,       8-128 chars)
    'type':                 (str,       8-128 chars)
    'wine':                 (int,       fk-->Wine<pk>)
    
    PERMISSIONS:
    authenticated:          (CREATE/RETRIEVE/UPDATE/DELETE)
    anonymous:              (RETRIEVE only)
    
    THROTTLES:
    create:                 (1/hour)
    </pre>
    """
    serializer_class = api_serializers.WineGlassSerializer
    queryset = api_models.WineGlass.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_classes = (api_throttles.CustomListCreateThrottle,)
    throttle_scope = 'glasscreate'
# /WineGlassViewSet


class LiquorGlassViewSet(viewsets.ModelViewSet):
    """
    <pre>
    Handles `liquor glass` resources.
    
    ATTRIBUTES:
    'name':                 (str,       8-128 chars)
    'type':                 (str,       8-128 chars)
    'liquor':               (int,       fk-->Liquor<pk>)
    
    PERMISSIONS:
    authenticated:          (CREATE/RETRIEVE/UPDATE/DELETE)
    anonymous:              (RETRIEVE only)
    
    THROTTLES:
    create:                 (1/hour)
    </pre>
    """
    serializer_class = api_serializers.LiquorGlassSerializer
    queryset = api_models.LiquorGlass.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_classes = (api_throttles.CustomListCreateThrottle,)
    throttle_scope = 'glasscreate'
# /LiquorGlassViewSet


class BeerStyleViewSet(viewsets.ModelViewSet):
    """
    <pre>
    Handles `beer style` resources.
    
    ATTRIBUTES:
    'name':                 (str,       8-128 chars)
    'description':          (str,       8-128 chars)
    'beer':                 (int,       fk-->Beer<pk>)
    
    PERMISSIONS:
    authenticated:          (CREATE/RETRIEVE/UPDATE/DELETE)
    anonymous:              (RETRIEVE only)
    
    THROTTLES:
    create:                 (1/day)
    </pre>
    """
    serializer_class = api_serializers.BeerStyleSerializer
    queryset = api_models.BeerStyle.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_classes = (api_throttles.CustomListCreateThrottle,)
    throttle_scope = 'stylecreate'
# /BeerStyleViewSet


class WineStyleViewSet(viewsets.ModelViewSet):
    """
    <pre>
    Handles `wine style` resources.
    
    ATTRIBUTES:
    'name':                 (str,       8-128 chars)
    'description':          (str,       8-128 chars)
    'wine':                 (int,       fk-->Wine<pk>)
    
    PERMISSIONS:
    authenticated:          (CREATE/RETRIEVE/UPDATE/DELETE)
    anonymous:              (RETRIEVE only)
    
    THROTTLES:
    create:                 (1/day)
    </pre>
    """
    serializer_class = api_serializers.WineStyleSerializer
    queryset = api_models.WineStyle.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_classes = (api_throttles.CustomListCreateThrottle,)
    throttle_scope = 'stylecreate'
# /WineStyleViewSet


class LiquorStyleViewSet(viewsets.ModelViewSet):
    """
    <pre>
    Handles `liquor style` resources.
    
    ATTRIBUTES:
    'name':                 (str,       8-128 chars)
    'description':          (str,       8-128 chars)
    'liquor':               (int,       fk-->Liquor<pk>)
    
    PERMISSIONS:
    authenticated:          (CREATE/RETRIEVE/UPDATE/DELETE)
    anonymous:              (RETRIEVE only)
    
    THROTTLES:
    create:                 (1/day)
    </pre>
    """
    serializer_class = api_serializers.LiquorStyleSerializer
    queryset = api_models.LiquorStyle.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_classes = (api_throttles.CustomListCreateThrottle,)
    throttle_scope = 'stylecreate'
# /LiquorStyleViewSet


class FavoriteViewSet(viewsets.ModelViewSet, NestedViewSetMixin):
    """
    <pre>
    Handles `favorite` resources.
    
    ATTRIBUTES:
    'favoriter':            (int,       fk-->User<pk>)
    'favorited':            (instance,  fk-->resource)
    
    PERMISSIONS:
    authenticated & owner:  (CREATE/DELETE)
    anonymous:              (RETRIEVE only)
    </pre>
    """
    serializer_class = api_serializers.FavoriteSerializer
    queryset = api_models.Favorite.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, 
                          api_permissions.IsOwnerOrReadOnly,)
    
    def pre_save(self, obj):
        obj.favoriter = self.request.user
# /FavoriteViewSet


class BeerReviewViewSet(viewsets.ModelViewSet, NestedViewSetMixin):
    """
    <pre>
    Handles `beer review` resources.
    
    ATTRIBUTES:
    'rater':                (int,       fk-->User<pk>)
    'title':                (str,       8-128 chars)
    'description':          (str,       8-1024 chars)
    'beer':                 (int,       fk-->Beer<pk>)
    'appearance':           (int,       1-5)
    'aroma':                (int,       1-5)
    'taste':                (int,       1-10)
    'palate':               (int,       1-5)
    'bottlestyle':          (int,       1-5)
    
    PERMISSIONS:
    authenticated & owner:  (CREATE/RETRIEVE/UPDATE/DELETE)
    anonymous:              (RETRIEVE)
    
    THROTTLES:
    create:                 (1/week)
    </pre>
    """
    serializer_class = api_serializers.BeerReviewSerializer
    queryset = api_models.BeerReview.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, 
                          api_permissions.IsOwnerOrReadOnly,)
    throttle_classes = (api_throttles.CustomListCreateThrottle,)
    throttle_scope = 'reviewcreate'
    
    def pre_save(self, obj):
        obj.rater = self.request.user
# /BeerReviewViewSet


class WineReviewViewSet(viewsets.ModelViewSet, NestedViewSetMixin):
    """
    <pre>
    Handles `wine review` resources.
    
    ATTRIBUTES:
    'rater':                (int,       fk-->User<pk>)
    'title':                (str,       8-128 chars)
    'description':          (str,       8-1024 chars)
    'wine':                 (int,       fk-->Wine<pk>)
    'clarity':              (int,       1-5)
    'color':                (int,       1-5)
    'intensity':            (int,       1-5)
    'aroma':                (int,       1-10)
    'body':                 (int,       1-5)
    'astringency':          (int,       1-5)
    'alcohol':              (int,       1-5)
    'balance':              (int,       1-10)
    'finish':               (int,       1-10)
    'complexity':           (int,       1-10)
    'bottlestyle':          (int,       1-5)
    
    PERMISSIONS:
    authenticated & owner:  (CREATE/RETRIEVE/UPDATE/DELETE)
    anonymous:              (RETRIEVE)
    
    THROTTLES:
    create:                 (1/week)
    </pre>
    """
    serializer_class = api_serializers.WineReviewSerializer
    queryset = api_models.WineReview.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, 
                          api_permissions.IsOwnerOrReadOnly,)
    throttle_classes = (api_throttles.CustomListCreateThrottle,)
    throttle_scope = 'reviewcreate'
    
    def pre_save(self, obj):
        obj.rater = self.request.user
# /WineReviewViewSet


class LiquorReviewViewSet(viewsets.ModelViewSet, NestedViewSetMixin):
    """
    <pre>
    Handles `liquor review` resources.
    
    ATTRIBUTES:
    'rater':                (int,       fk-->User<pk>)
    'title':                (str,       8-128 chars)
    'description':          (str,       8-1024 chars)
    'liquor':               (int,       fk-->Liquor<pk>)
    'appearance':           (int,       1-5)
    'aroma':                (int,       1-5)
    'taste':                (int,       1-10)
    'aftertaste':           (int,       1-5)
    
    PERMISSIONS:
    authenticated & owner:  (CREATE/RETRIEVE/UPDATE/DELETE)
    anonymous:              (RETRIEVE)
    
    THROTTLES:
    create:                 (1/week)
    </pre>
    """
    serializer_class = api_serializers.LiquorReviewSerializer
    queryset = api_models.LiquorReview.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, 
                          api_permissions.IsOwnerOrReadOnly,)
    throttle_classes = (api_throttles.CustomListCreateThrottle,)
    throttle_scope = 'reviewcreate'
    
    def pre_save(self, obj):
        obj.rater = self.request.user
# /LiquorReviewViewSet


class UserViewSet(viewsets.ModelViewSet, NestedViewSetMixin):
    """
    <pre>
    Handles `user` resources.
    </pre>
    """
    serializer_class = api_serializers.UserSerializer
    queryset = User.objects.filter(is_superuser=False, 
                                   is_staff=False).order_by('-last_login')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, 
                          api_permissions.IsOwnerOrReadOnly,)
    
    def pre_save(self, obj):
        obj.rater = self.request.user
# /UserViewSet


#EOF - publican_api views