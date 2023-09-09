"""publican_api views"""

from django.db import models
from django.db.models import Q
from django.http import Http404
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.contrib.contenttypes.models import ContentType

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import publican_api.models as api_models
import publican_api.serializers as api_serializers
import publican_api.utils as api_utils


class DrinkListView(generics.ListAPIView):
    """
    List beers, wines, or liquors.
    Drink type is determined by drink parameter.
    No throttling.
    Permit anonymous and authenticated users to list drinks.
    """
    def get_queryset(self):
        app_label = api_utils.get_app_label()
        drink = self.kwargs['drink']
        drink_type = ContentType.objects.get(app_label=app_label, model=drink)
        drink_model = drink_type.model_class()
        queryset = drink_model.objects.all()
        return queryset
    
    def get_serializer_class(self):
        drink = self.kwargs['drink'].capitalize() + "Serializer"
        serializer = getattr(api_serializers, drink)
        return serializer
    
    permission_classes = (IsAuthenticatedOrReadOnly,)
# /DrinkListView


class DrinkCreateView(generics.CreateAPIView):
    """
    Create a beer, wine, or liquor.
    Drink type is determined by drink parameter.
    Throttle drink creations to < 1/day.
    Permit only authenticated users to create drinks.
    """
    def get_serializer_class(self):
        drink = self.kwargs['drink'].capitalize() + "Serializer"
        serializer = getattr(api_serializers, drink)
        return serializer
    
    throttle_classes = (DrinkCreateRateThrottle,)
    permission_classes = (IsAuthenticated,)
# /DrinkCreateThrottledView


class DrinkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a beer, wine, or liquor instance.
    Drink type is determined by drink parameter.
    Specific drink is queried by either pk or slug determined by id parameter.
    Permit anonymous and authenticated users to retrieve drinks.
    Permit only authenticated users to update or delete drinks.
    """
    def get_queryset(self):
        app_label = api_utils.get_app_label()
        drink = self.kwargs['drink']
        drink_id = self.kwargs['drink_id']
        drink_type = ContentType.objects.get(app_label=app_label, model=drink)
        drink_model = drink_type.model_class()
        queryset = drink_model.objects.get(Q(slug=drink_id) | Q(pk=drink_id))
        return queryset
            
    def get_serializer_class(self):
        drink = self.kwargs['drink'].capitalize() + "Serializer"
        serializer = getattr(api_serializers, drink)
        return serializer
    
    permission_classes = (IsAuthenticatedOrReadOnly,)
# /DrinkCreateThrottledView


class FacilityListView(generics.ListAPIView):
    """
    List breweries, wineries, or distilleries.
    Facility type is determined by drink parameter.
    No throttling.
    Permit anonymous and authenticated users to list facilities.
    """
    def get_queryset(self):
        app_label = api_utils.get_app_label()
        facility = self.kwargs['facility']
        facility_type = ContentType.objects.get(app_label=app_label, model=facility)
        facility_model = facility_type.model_class()
        queryset = facility_model.objects.all()
        return queryset
    
    def get_serializer_class(self):
        facility = self.kwargs['facility'].capitalize() + "Serializer"
        serializer = getattr(api_serializers, facility)
        return serializer
    
    permission_classes = (IsAuthenticatedOrReadOnly,)
# /FacilityListView


class FacilityCreateView(generics.CreateAPIView):
    """
    Create a brewery, winery, or distillery.
    Facility type is determined by drink parameter.
    Throttle facility creations to < 1/hour.
    Permit only authenticated users to create facilities.
    """
    def get_serializer_class(self):
        facility = self.kwargs['facility'].capitalize() + "Serializer"
        serializer = getattr(api_serializers, facility)
        return serializer
    
    throttle_classes = (FacilityCreateRateThrottle,)
    permission_classes = (IsAuthenticated,)
# /FacilityCreateView


class FacilityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a brewery, winery, or distillery instance.
    Facility type is determined by drink parameter.
    Specific facility is queried by either pk or slug, determined by id parameter.
    Permit anonymous and authenticated users to retrieve facilities.
    Permit only authenticated users to update or delete facilities.
    """
    def get_queryset(self):
        app_label = api_utils.get_app_label()
        facility = self.kwargs['facility']
        facility_id = self.kwargs['facility_id']
        facility_type = ContentType.objects.get(app_label=app_label, model=facility)
        facility_model = facility_type.model_class()
        queryset = facility_model.objects.get(Q(slug=facility_id) | Q(pk=facility_id))
        return queryset
    
    def get_serializer_class(self):
        facility = self.kwargs['facility'].capitalize() + "Serializer"
        serializer = getattr(api_serializers, facility)
        return serializer
    
    permission_classes = (IsAuthenticatedOrReadOnly,)
# /FacilityRetrieveUpdateDestroyView


class GlassListView(generics.ListAPIView):
    """
    List beer, wine, or liquor glasses.
    Glass type is determined by drink parameter.
    No throttling.
    Permit anonymous and authenticated users to list glasses.
    """
    def get_queryset(self):
        app_label = api_utils.get_app_label()
        glass = self.kwargs['glass']
        glass_type = ContentType.objects.get(app_label=app_label, model=glass)
        glass_model = glass_type.model_class()
        queryset = glass_model.objects.all()
        return queryset
    
    def get_serializer_class(self):
        glass = self.kwargs['glass'].capitalize() + "Serializer"
        serializer = getattr(api_serializers, glass)
        return serializer
    
    permission_classes = (IsAuthenticatedOrReadOnly,)
# /GlassListView


class GlassCreateView(generics.CreateAPIView):
    """
    Create a beer, wine, or liquor glass.
    Glass type is determined by drink parameter.
    Throttle glass creations to < 1/minute.
    Permit only authenticated users to create glasses.
    """
    def get_serializer_class(self):
        glass = self.kwargs['glass'].capitalize() + "Serializer"
        serializer = getattr(api_serializers, glass)
        return serializer
    
    throttle_classes = (GlassCreateRateThrottle,)
    permission_classes = (IsAuthenticated,)
# /GlassCreateView


class GlassRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a beer, wine, or liquor glass instance.
    Glass type is determined by drink parameter.
    Specific glass is queried by either pk or slug, determined by id parameter.
    Permit anonymous and authenticated users to retrieve glasses.
    Permit only authenticated users to update or delete glasses.
    """
    def get_queryset(self):
        app_label = api_utils.get_app_label()
        glass = self.kwargs['glass']
        glass_id = self.kwargs['glass_id']
        glass_type = ContentType.objects.get(app_label=app_label, model=glass)
        glass_model = glass_type.model_class()
        queryset = glass_model.objects.get(Q(slug=glass_id) | Q(pk=glass_id))
        return queryset
    
    def get_serializer_class(self):
        glass = self.kwargs['glass'].capitalize() + "Serializer"
        serializer = getattr(api_serializers, glass)
        return serializer
    
    permission_classes = (IsAuthenticatedOrReadOnly,)
# /GlassRetrieveUpdateDestroyView


class StyleListView(generics.ListAPIView):
    """
    List beer, wine, or liquor styles.
    Style type is determined by drink parameter.
    No throttling.
    Permit anonymous and authenticated users to list styles.
    """
    def get_queryset(self):
        app_label = api_utils.get_app_label()
        style = self.kwargs['style']
        style_type = ContentType.objects.get(app_label=app_label, model=style)
        style_model = style_type.model_class()
        queryset = style_model.objects.all()
        return queryset
    
    def get_serializer_class(self):
        style = self.kwargs['style'].capitalize() + "Serializer"
        serializer = getattr(api_serializers, style)
        return serializer
    
    permission_classes = (IsAuthenticatedOrReadOnly,)
# /StyleListView


class StyleCreateView(generics.CreateAPIView):
    """
    Create a beer, wine, or liquor.
    Drink type is determined by drink parameter.
    Throttle drink creations to < 1/day.
    Permit only authenticated users to create drinks.
    """
    def get_serializer_class(self):
        style = self.kwargs['style'].capitalize() + "Serializer"
        serializer = getattr(api_serializers, style)
        return serializer
    
    throttle_classes = (StyleCreateRateThrottle,)
    permission_classes = (IsAuthenticated,)
# /StyleCreateView


class StyleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a beer, wine, or liquor instance.
    Drink type is determined by drink parameter.
    Specific drink is queried by either pk or slug, determined by id parameter.
    Permit anonymous and authenticated users to retrieve drinks.
    Permit only authenticated users to update or delete drinks.
    """
    def get_queryset(self):
        app_label = api_utils.get_app_label()
        style = self.kwargs['style']
        style_id = self.kwargs['style_id']
        style_type = ContentType.objects.get(app_label=app_label, model=style)
        style_model = style_type.model_class()
        queryset = style_model.objects.get(Q(slug=style_id) | Q(pk=style_id))
        return queryset
    
    def get_serializer_class(self):
        style = self.kwargs['style'].capitalize() + "Serializer"
        serializer = getattr(api_serializers, style)
        return serializer
    
    permission_classes = (IsAuthenticatedOrReadOnly,)
# /StyleRetrieveUpdateDestroyView


class ReviewListView(generics.ListAPIView):
    """
    List beer, wine, or liquor reviews.
    Review type is determined by drink parameter.
    No throttling.
    Permit anonymous and authenticated users to list reviews.
    """
    def get_queryset(self):
        app_label = api_utils.get_app_label()
        review = self.kwargs['review']
        review_type = ContentType.objects.get(app_label=app_label, model=review)
        review_model = review_type.model_class()
        queryset = review_model.objects.all()
        return queryset
    
    def get_serializer_class(self):
        review = self.kwargs['review'].capitalize() + "Serializer"
        serializer = getattr(api_serializers, review)
        return serializer
    
    permission_classes = (IsAuthenticatedOrReadOnly,)
# /ReviewListView


class ReviewCreateView(generics.CreateAPIView):
    """
    Create a beer, wine, or liquor review.
    Review type is determined by drink parameter.
    Throttle review creations to < 1/day.
    Permit only authenticated users to create reviews.
    """
    def get_serializer_class(self):
        review = self.kwargs['review'].capitalize() + "Serializer"
        serializer = getattr(api_serializers, review)
        return serializer
    
    throttle_classes = (DrinkReviewCreateRateThrottle,)
    permission_classes = (IsAuthenticated,)
# /ReviewCreateView


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a beer, wine, or liquor review instance.
    Review type is determined by drink parameter.
    Specific review is queried by either pk or slug, determined by id parameter.
    Permit anonymous and authenticated users to retrieve reviews.
    Permit only authenticated users to update or delete reviews.
    """
    def get_queryset(self):
        app_label = api_utils.get_app_label()
        review = self.kwargs['review']
        review_id = self.kwargs['review_id']
        review_type = ContentType.objects.get(app_label=app_label, model=review)
        review_model = review_type.model_class()
        queryset = review_model.objects.get(Q(slug=review_id) | Q(pk=review_id))
        return queryset
    
    def get_serializer_class(self):
        review = self.kwargs['review'].capitalize() + "Serializer"
        serializer = getattr(api_serializers, review)
        return serializer
    
    permission_classes = (IsAuthenticatedOrReadOnly,)
# /ReviewRetrieveUpdateDestroyView


class UserListCreate(generics.ListCreateAPIView):
    """
    Create a user or list users.
    """
    queryset = User.objects.all().order('-last_login')
    serializer_class = UserSerializer
    
    # def pre_save(self, obj):
        # user = obj
        # serializer = UserSerializer(data=request.DATA)
        # if serializer.is_valid():
            # user.set_password(serializer.data['password'])
# /UserListCreate


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a registered user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
# /UserRetrieveUpdateDestroy


class FavoritesList(APIView):
    """
    """
    authentication_classes = (authentication.IsAuthenticatedOrReadOnly,)
    
    def get_serializer(self, entity_model=None):
        entity_serializer_name = entity_model.__name__.capitalize() + "Serializer"
        entity_serializer = getattr(api_serializers, entity_serializer_name)
        return entity_serializer
    
    
    def get(self, request, user_id=None, entity=None):
        app_label = api_utils.get_app_label()
        
        publican_user = User.objects.get(Q(pk=user_id) | Q(username=user_id))
        if entity is not None:
            entity_type = ContentType.objects.get(app_label=app_label, model=entity)
            entity_model = entity_type.model_class()
            publican_items = entity_model.objects.filter(favorite_of=publican_user)
            item_serializer = self.get_serializer(entity)
            serializer = item_serializer(publican_items, many=True)
        else:
            app_models = [model.__name__.replace('_favorite_of', '') 
                          for model in models.get_models(include_auto_created=True) 
                          if 'favorite_of' in model.__name__ 
                          and model._meta.app_label == app_label]
            serialized_items = []
            for entity_model in entity_models:
                publican_items = models.get_model('publican_api', model_name=entity_model)
                                       .objects.filter(favorite_of=publican_user)
                item_serializer = self.get_serializer(entity)
                serializer = item_serializer(publican_items, many=True)
                serialized_items.append(serializer.data)
        
        return Response(serialized_items)
# /FavoritesList
        
    
# @api_view(['GET'])
# @authentication_classes(['IsAuthenticatedOrReadOnly,'])
# def listfavorite(request, user_id=None, item=None):
    # _app_label = api_utils.get_app_label()
    # _user_id = user_id
    # _item = item
    
    # publican_user = User.objects.get(Q(pk=_user_id) | Q(username=_user_id))
    # if _item is not None:
        # _item_type = ContentType.objects.get(app_label=_app_label, model=_item)
        # _item_model = _item_type.model_class()
        # publican_items = _item_model.objects.filter(favorite_of=publican_user)
    # else:
        #SOMEHOW LIST ALL FAVORITES FOR USER FOR ALL ITEMS
        # _app_models = [_model.__name__.replace('_favorite_of', '') 
                       # for _model in models.get_models(include_auto_created=True) 
                       # if 'favorite_of' in _model.__name__ 
                       # and _model._meta.app_label == _app_label]

        # publican_items = []
        # for _app_model in _app_models:
           # publican_items += models.get_model('publican_api', model_name=_app_model)
                             # .objects.filter(favorite_of=publican_user)


class FavoritesDetail(APIView):
    """
    """
    authentication_classes = (authentication.IsAuthenticated,)
    
    def get_object(self, entity=None, entity_id=None):
        app_label = api_utils.get_app_label()
        
        entity_type = ContentType.objects.get(app_label=app_label, model=entity)
        entity_model = entity_type.model_class()
        try:
            return entity_model.objects.get(Q(slug=entity_id) | Q(pk=entity_id))
        except entity_model.DoesNotExist:
            raise Http404
    
    def get_user(self, user_id=None):
        try:
            user = User.objects.get(Q(slug=user_id) | Q(pk=user_id))
        except User.DoesNotExist:
            raise Http404
    
    def get_serializer(self, entity=None):
        entity_serializer_name = entity.capitalize() + "Serializer"
        entity_serializer = getattr(api_serializers, entity_serializer_name)
        return entity_serializer
    
    
    def get(self, request, user_id=None, entity=None):
        publican_item = self.get_object(entity, entity_id)
        item_serializer = self.get_serializer(entity)
        serializer = item_serializer(publican_item)
        return Response(serializer.data)
    
    def put(self, request, user_id=None, entity=None, entity_id=None):
        publican_item = self.get_object(entity, entity_id)
        publican_user = self.get_user(user_id)
        if publican_user not in publican_item.favorite_of.all():
            publican_item.favorite_of.add(publican_user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, user_id=None, entity=None, entity_id=None):
        publican_item = self.get_object(entity, entity_id)
        if publican_user in publican_item.favorite_of.all():
            publican_item.favorite_of.remove(publican_user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
# /FavoritesDetail


# @api_view(['POST', 'PUT', 'PATCH'])
# @authentication_classes(['IsAuthenticated,'])
# def togglefavorite(request, user_id=None, item=None, item_id=None):
    # _app_label = api_utils.get_app_label()
    # _user_id = user_id
    # _item = item
    # _item_id = item_id
    
    # item_type = ContentType.objects.get(app_label=_app_label, model=_item)
    # item_model = item_type.model_class()
    # publican_item = item_model.objects.get(Q(slug=_item_id) | Q(pk=_item_id))
    # publican_user = User.objects.get(Q(pk=_user_id) | Q(username=_user_id))
    
    # if publican_user in publican_item.favorite_of.all():
        # publican_item.favorite_of.remove(publican_user)
    # else:
        # publican_item.favorite_of.add(publican_user)
# /togglefavorite
    

class DocumentRetrieveView(generics.RetrieveAPIView):
    """
    Retrieve an API document, including installation instructions, execution 
    instructions, software requirements, endpoint definitions, API base models 
    source, API models source, API views source, API serializers source, 
    API throttles source, and/or API permissions source.
    Permit only read-only document endpoints.
    Permit only authenticated users to retrieve documents.
    """
    def get_queryset(self):
        app_label = api_utils.get_app_label()
        document = self.kwargs['document']
        document_id = self.kwargs['document_id']
        document_type = ContentType.objects.get(app_label=app_label, model=document)
        document_model = document_type.model_class()
        queryset = document_model.objects.get(Q(slug=document_id) | Q(pk=document_id))
        return queryset
    
    
    def get_serializer_class(self):
        document = self.kwargs['document'].capitalize() + "Serializer"
        serializer = getattr(api_serializers, document)
        return serializer
    
    permission_classes = (IsAuthenticated,)
# /DocumentRetrieveView

                     
# EOF - publican_api views