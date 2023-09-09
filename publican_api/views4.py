"""publican_api views"""

from django.db import models
from django.db.models import Q
from django.http import Http404
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.contrib.contenttypes.models import ContentType

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status

import publican_api.models as api_models
import publican_api.serializers as api_serializers
import publican_api.throttles as api_throttles
import publican_api.utils as api_utils


class DrinkListCreateView(generics.ListCreateAPIView):
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
        try:
            return drink_model.objects.all()
        except drink_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        drink = self.kwargs['drink'].capitalize() + "Serializer"
        return getattr(api_serializers, drink)
    
    throttle_classes = (api_throttles.DrinkCreateRateThrottle,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# /DrinkListCreateView


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
        try:
            return drink_model.objects.get(Q(slug=drink_id) | Q(pk=int(drink_id)))
        except drink_model.DoesNotExist:
            raise Http404
            
    def get_serializer_class(self):
        drink = self.kwargs['drink'].capitalize() + "Serializer"
        return getattr(api_serializers, drink)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# /DrinkRetrieveUpdateDestroyView


class FacilityListCreateView(generics.ListCreateAPIView):
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
        try:
            return facility_model.objects.all()
        except facility_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        facility = self.kwargs['facility'].capitalize() + "Serializer"
        return getattr(api_serializers, facility)
    
    throttle_classes = (api_throttles.FacilityCreateRateThrottle,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# /FacilityListCreateView


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
        try:
            return facility_model.objects.get(Q(slug=facility_id) | Q(pk=int(facility_id)))
        except facility_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        facility = self.kwargs['facility'].capitalize() + "Serializer"
        return getattr(api_serializers, facility)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# /FacilityRetrieveUpdateDestroyView


class GlassListCreateView(generics.ListCreateAPIView):
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
        try:
            return glass_model.objects.all()
        except glass_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        glass = self.kwargs['glass'].capitalize() + "Serializer"
        return getattr(api_serializers, glass)
    
    throttle_classes = (api_throttles.GlassCreateRateThrottle,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# /GlassListCreateView


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
        try:
            return glass_model.objects.get(Q(slug=glass_id) | Q(pk=int(glass_id)))
        except glass_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        glass = self.kwargs['glass'].capitalize() + "Serializer"
        return getattr(api_serializers, glass)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# /GlassRetrieveUpdateDestroyView


class StyleListCreateView(generics.ListCreateAPIView):
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
        try:
            return style_model.objects.all()
        except style_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        style = self.kwargs['style'].capitalize() + "Serializer"
        return getattr(api_serializers, style)
    
    throttle_classes = (api_throttles.StyleCreateRateThrottle,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# /StyleListCreateView


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
        try:
            return style_model.objects.get(Q(slug=style_id) | Q(pk=int(style_id)))
        except style_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        style = self.kwargs['style'].capitalize() + "Serializer"
        return getattr(api_serializers, style)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# /StyleRetrieveUpdateDestroyView


class ReviewListCreateView(generics.ListAPIView):
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
        try:
            return review_model.objects.all()
        except review_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        review = self.kwargs['review'].capitalize() + "Serializer"
        return getattr(api_serializers, review)
    
    throttle_classes = (api_throttles.DrinkReviewRateThrottle,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# /ReviewListCreateView


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
        try:
            return review_model.objects.get(Q(slug=review_id) | Q(pk=int(review_id)))
        except review_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        review = self.kwargs['review'].capitalize() + "Serializer"
        return getattr(api_serializers, review)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# /ReviewRetrieveUpdateDestroyView


class UserListCreate(generics.ListCreateAPIView):
    """
    Create a user or list users.
    """
    queryset = User.objects.all().order_by('-last_login')
    serializer_class = api_serializers.UserSerializer
    
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
    serializer_class = api_serializers.UserSerializer
# /UserRetrieveUpdateDestroy


class FavoriteList(APIView):
    """
    """
    
    def get_serializer(self, entity_model=None):
        entity_serializer_name = entity_model.__name__.capitalize() + "Serializer"
        entity_serializer = getattr(api_serializers, entity_serializer_name)
        return entity_serializer
    
    
    def get(self, request, user_id=None, entity=None):
        app_label = api_utils.get_app_label()
        
        publican_user = User.objects.get(Q(pk=int(user_id)) | Q(username=user_id))
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
                publican_items = models.get_model(
                                        'publican_api', model_name=entity_model
                                       ).objects.filter(favorite_of=publican_user)
                item_serializer = self.get_serializer(entity)
                serializer = item_serializer(publican_items, many=True)
                serialized_items.append(serializer.data)
        
        return Response(serialized_items)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# /FavoriteList


class FavoriteDetail(APIView):
    """
    """
    
    def get_object(self, entity=None, entity_id=None):
        app_label = api_utils.get_app_label()
        
        entity_type = ContentType.objects.get(app_label=app_label, model=entity)
        entity_model = entity_type.model_class()
        try:
            return entity_model.objects.get(Q(slug=entity_id) | Q(pk=int(entity_id)))
        except entity_model.DoesNotExist:
            raise Http404
    
    def get_user(self, user_id=None):
        try:
            user = User.objects.get(Q(slug=user_id) | Q(pk=int(user_id)))
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
    
    permission_classes = (permissions.IsAuthenticated,)
# /FavoriteDetail


class DocumentListView(generics.RetrieveAPIView):
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
        
        documents = []
        for model in dir(api.models):
            document_model = getattr(api.models, model)
            if issubclass(document_model, api_basemodels.Document):
                try:
                    documents.append(document_model.objects.all())
                except document_model.DoesNotExist:
                    raise Http404
        return documents
    
    def get_serializer_class(self):
        document = self.kwargs['document'].capitalize() + "Serializer"
        return getattr(api_serializers, document)
    
    permission_classes = (permissions.IsAuthenticated,)
# /DocumentListView


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
        try:
            return document_model.objects.get(Q(slug=document_id) | Q(pk=int(document_id)))
        except document_model.DoesNotExist:
            raise Http404
    
    
    def get_serializer_class(self):
        document = self.kwargs['document'].capitalize() + "Serializer"
        return getattr(api_serializers, document)
    
    permission_classes = (permissions.IsAuthenticated,)
# /DocumentRetrieveView

                     
# EOF - publican_api views