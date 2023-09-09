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
import publican_api.permissions as api_permissions
import publican_api.throttles as api_throttles
import publican_api.utils as api_utils


def get_model_by_slug(slug_name=None):
    app_label = api_utils.get_app_label()
    try:
        model_type = ContentType.objects.get(app_label=app_label, model=slug_name)
    except KeyError:
        return ""
    return model_type.model_class()


class APIRoot(views.APIView):
    _ignore_model_permissions = True

    def get(self, request, format=None):
        ret = {}
        for key, url_name in api_root_dict.items():
            ret[key] = reverse(url_name, request=request, format=format)
        return Response(ret)


class DrinkListCreateView(generics.ListCreateAPIView):
    """
    List beers, wines, or liquors.
    Drink type is determined by drink parameter.
    Throttle drink creations to < 1/day.
    No throttling for drink listings.
    Permit only authenticated users to create drinks.
    Permit anonymous and authenticated users to list drinks.
    """
    def get_queryset(self):
        drink = self.kwargs['drink']
        drink_model = get_model_by_slug(drink)
        try:
            return drink_model.objects.all()
        except drink_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        drink = self.kwargs['drink']
        drink_serializer = get_model_by_slug(drink).__name__ + "Serializer"
        return getattr(api_serializers, drink_serializer)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_classes = (api_throttles.CustomListCreateThrottle,)
    throttle_scope = 'drinkcreate'
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
        drink = self.kwargs['drink']
        drink_id = self.kwargs['drink_id']
        drink_model = get_model_by_slug(drink)
        try:
            return drink_model.objects.get(Q(slug=drink_id) | Q(pk=int(drink_id)))
        except drink_model.DoesNotExist:
            raise Http404
            
    def get_serializer_class(self):
        drink = self.kwargs['drink']
        drink_serializer = get_model_by_slug(drink).__name__ + "Serializer"
        return getattr(api_serializers, drink_serializer)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# /DrinkRetrieveUpdateDestroyView


class FacilityListCreateView(generics.ListCreateAPIView):
    """
    List breweries, wineries, or distilleries.
    Facility type is determined by drink parameter.
    Throttle facility creations to < 1/hour.
    No throttling for facility listings.
    Permit only authenticated users to create facilities.
    Permit anonymous and authenticated users to list facilities.
    """
    def get_queryset(self):
        facility = self.kwargs['facility']
        facility_model = get_model_by_slug(facility)
        try:
            return facility_model.objects.all()
        except facility_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        facility = self.kwargs['facility']
        facility_serializer = get_model_by_slug(facility).__name__ + "Serializer"
        return getattr(api_serializers, facility_serializer)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_classes = (api_throttles.CustomListCreateThrottle,)
    throttle_scope = 'facilitycreate'
# /FacilityListCreateView


class FacilityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a brewery, winery, or distillery instance.
    Facility type is determined by drink parameter.
    Specific facility is queried by either pk or slug, determined by id parameter.
    Permit only authenticated users to update or delete facilities.
    Permit anonymous and authenticated users to retrieve facilities.
    """
    def get_queryset(self):
        facility = self.kwargs['facility']
        facility_id = self.kwargs['facility_id']
        facility_model = get_model_by_slug(facility)
        try:
            return facility_model.objects.get(Q(slug=facility_id) | Q(pk=int(facility_id)))
        except facility_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        facility = self.kwargs['facility']
        facility_serializer = get_model_by_slug(facility).__name__ + "Serializer"
        return getattr(api_serializers, facility_serializer)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# /FacilityRetrieveUpdateDestroyView


class GlassListCreateView(generics.ListCreateAPIView):
    """
    List beer, wine, or liquor glasses.
    Glass type is determined by drink parameter.
    Throttle glass creations to < 1/minute.
    No throttling for glass listings.
    Permit only authenticated users to create glasses.
    Permit anonymous and authenticated users to list glasses.
    """
    def get_queryset(self):
        glass = self.kwargs['glass']
        glass_model = get_model_by_slug(glass)
        try:
            return glass_model.objects.all()
        except glass_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        glass = self.kwargs['glass']
        glass_serializer = get_model_by_slug(glass).__name__ + "Serializer"
        return getattr(api_serializers, glass_serializer)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_classes = (api_throttles.CustomListCreateThrottle,)
    throttle_scope = 'glasscreate'
# /GlassListView


class GlassRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a beer, wine, or liquor glass instance.
    Glass type is determined by drink parameter.
    Specific glass is queried by either pk or slug, determined by id parameter.
    Permit anonymous and authenticated users to retrieve glasses.
    Permit only authenticated users to update or delete glasses.
    """
    def get_queryset(self):
        glass = self.kwargs['glass']
        glass_id = self.kwargs['glass_id']
        glass_model = get_model_by_slug(glass)
        try:
            return glass_model.objects.get(Q(slug=glass_id) | Q(pk=int(glass_id)))
        except glass_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        glass = self.kwargs['glass']
        glass_serializer = get_model_by_slug(glass).__name__ + "Serializer"
        return getattr(api_serializers, glass_serializer)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# /GlassRetrieveUpdateDestroyView


class StyleListCreateView(generics.ListCreateAPIView):
    """
    List or create beer, wine, or liquor styles.
    Style type is determined by drink parameter.
    Throttle drink creations to < 1/day.
    No throttling for glass listings.
    Permit only authenticated users to create styles.
    Permit both anonymous and authenticated users to list styles.
    """
    def get_queryset(self):
        style = self.kwargs['style']
        style_model = get_model_by_slug(style)
        try:
            return style_model.objects.all()
        except style_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        style = self.kwargs['style']
        style_serializer = get_model_by_slug(style).__name__ + "Serializer"
        return getattr(api_serializers, style_serializer)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_classes = (api_throttles.CustomListCreateThrottle,)
    throttle_scope = 'stylecreate'
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
        style = self.kwargs['style']
        style_id = self.kwargs['style_id']
        style_model = get_model_by_slug(style)
        try:
            return style_model.objects.get(Q(slug=style_id) | Q(pk=int(style_id)))
        except style_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        style = self.kwargs['style']
        style_serializer = get_model_by_slug(style).__name__ + "Serializer"
        return getattr(api_serializers, style_serializer)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# /StyleRetrieveUpdateDestroyView


class ReviewListCreateView(generics.ListCreateAPIView):
    """
    List beer, wine, or liquor reviews.
    Review type is determined by drink parameter.
    Throttle drink reviews to < 1/week.
    No throttling for review listings.
    Permit only authenticated users to review drinks.
    Permit both anonymous and authenticated users to list drink reviews.
    """
    def get_queryset(self):
        review = self.kwargs['review']
        review_model = get_model_by_slug(review)
        try:
            return review_model.objects.all()
        except review_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        review = self.kwargs['review']
        review_serializer = get_model_by_slug(review).__name__ + "Serializer"
        return getattr(api_serializers, review_serializer)
    
    def pre_save(self, obj):
        obj.rater = self.request.user
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_classes = (api_throttles.CustomListCreateThrottle,)
    throttle_scope = 'reviewcreate'
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
        review = self.kwargs['review']
        review_id = self.kwargs['review_id']
        review_model = get_model_by_slug(review)
        try:
            obj = review_model.objects.get(Q(slug=review_id) | Q(pk=int(review_id)))
            self.check_object_permissions(self.request, obj)
            return obj
        except review_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        review = self.kwargs['review']
        review_serializer = get_model_by_slug(review).__name__ + "Serializer"
        return getattr(api_serializers, review_serializer)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, 
                          api_permissions.IsOwnerOrReadOnly,)
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
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        try:
            user = User.objects.get(Q(slug=user_id) | Q(pk=int(user_id)))
        except User.DoesNotExist:
            raise Http404
        return user
    
    serializer_class = api_serializers.UserSerializer
# /UserRetrieveUpdateDestroy


class FavoriteList(APIView):
    """
    """
    
    def get_user(self, user_id=None):
        try:
            user = User.objects.get(Q(slug=user_id) | Q(pk=int(user_id)))
        except User.DoesNotExist:
            raise Http404
    
    def get_serializer(self, entity=None):
        entity_serializer = get_model_by_slug(entity).__name__ + "Serializer"
        return getattr(api_serializers, entity_serializer)
    
    
    def get(self, request, user_id=None, entity=None):
        app_label = api_utils.get_app_label()
        publican_user = self.get_user(user_id)
        #Is this a listing of favorites for one entity or for all entities?
        if entity is not None:
            entity_model = get_model_by_slug(entity)
            publican_items = entity_model.objects.filter(favorite_of=publican_user)
            item_serializer = self.get_serializer(entity)
            serializer = item_serializer(publican_items, many=True)
            serialized_items = serializer.data
        else:
            entity_models = [model.__name__.replace('_favorite_of', '') 
                             for model in models.get_models(include_auto_created=True) 
                             if 'favorite_of' in model.__name__ 
                             and model._meta.app_label == app_label]
            serialized_items = []
            for entity_model in entity_models:
                publican_items += models.get_model(
                                         app_label, model_name=entity_model
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
        entity_model = get_model_by_slug(entity)
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
        entity_serializer = get_model_by_slug(entity).__name__ + "Serializer"
        return getattr(api_serializers, entity_serializer)
    
    
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


class ReviewList(APIView):
    """
    """
    
    def get_user(self, user_id=None):
        try:
            user = User.objects.get(Q(slug=user_id) | Q(pk=int(user_id)))
        except User.DoesNotExist:
            raise Http404
    
    def get_serializer(self, entity=None):
        entity_serializer = get_model_by_slug(entity) + "ReviewSerializer"
        return getattr(api_serializers, entity_serializer)
    
    
    def get(self, request, user_id=None, entity=None):
        app_label = api_utils.get_app_label()
        
        publican_user = self.get_user(user_id)
        #Is this a listing of favorites for one entity or for all entities?
        if entity is not None:
            review = entity.capitalize() + "Review"
            review_model = get_model_by_slug(review)
            try:
                publican_reviews = review_model.objects.filter(rater__id=user.id)
            except review_model.DoesNotExist:
                raise Http404
            review_serializer = self.get_serializer(entity)
            serializer = review_serializer(publican_reviews, many=True)
            serialized_items = serializer.data
        else:
            app_models = [model.__name__ 
                          for model in models.get_models(include_auto_created=True) 
                          if issubclass(model, api_basemodels.Review) 
                          and model._meta.app_label == app_label]
            serialized_items = []
            for entity_model in entity_models:
                publican_items = models.get_model(
                                        app_label, model_name=entity_model
                                       ).objects.filter(favorite_of=publican_user)
                item_serializer = self.get_serializer(entity)
                serializer = item_serializer(publican_items, many=True)
                serialized_items.append(serializer.data)
        
        return Response(serialized_items)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# /ReviewList


class ReviewDetail(APIView):
    """
    """
    
    def get_object(self, user=None, entity=None, entity_id=None):
        entity_model = get_model_by_slug(entity)
        try:
            item = entity_model.objects.get(Q(slug=entity_id) | Q(pk=int(entity_id)))
        except entity_model.DoesNotExist:
            raise Http404
        review = entity.capitalize() + "Review"
        review_model = get_model_by_slug(review)
        try:
            return review_model.objects.get(rater__id=user.id, drink__id=item.id)
        except review_model.DoesNotExist:
            raise Http404
    
    def get_user(self, user_id=None):
        try:
            user = User.objects.get(Q(slug=user_id) | Q(pk=int(user_id)))
        except User.DoesNotExist:
            raise Http404
    
    def get_serializer(self, entity=None):
        entity_serializer = get_model_by_slug(entity) + "ReviewSerializer"
        return getattr(api_serializers, entity_serializer)
    
    
    def get(self, request, user_id=None, entity=None, entity_id=None):
        publican_user = self.get_user(user_id)
        publican_review = self.get_object(publican_user, entity, entity_id)
        review_serializer = self.get_serializer(entity)
        serializer = review_serializer(publican_review)
        return Response(serializer.data)
    
    permission_classes = (permissions.IsAuthenticated,)
# /ReviewDetail

                     
# EOF - publican_api views