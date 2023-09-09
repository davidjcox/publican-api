"""publican_api views"""

from operator import itemgetter
from collections import OrderedDict

from django.db import models
from django.db.models import Q
from django.http import Http404
from django.contrib.auth.models import User
from django.core.urlresolvers import NoReverseMatch
from django.db.models.fields.related import ForeignKey
from django.contrib.contenttypes.models import ContentType

from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status

import publican_api.models as api_models
import publican_api.basemodels as api_basemodels
import publican_api.serializers as api_serializers
import publican_api.permissions as api_permissions
import publican_api.throttles as api_throttles
import publican_api.utils as api_utils


def get_model_by_slug(slug_name=None):
    """
    Transform slug_name into model name, look up model, and return it.
    """
    app_label = api_utils.get_app_label()
    entity_name = ""
    model_name = ""
    if slug_name is not None:
        entity_name = slug_name.replace("-", " ").lower()
    entity_model = [model._meta.verbose_name for model in models.get_models() 
                    if model._meta.app_label == app_label 
                    and model._meta.verbose_name_plural == entity_name]
    if entity_model is not None:
        model_name = entity_model[0].replace(" ", "")
    try:
        model_type = ContentType.objects.get(app_label=app_label, model=model_name)
    except:
        return None
    return model_type.model_class()


class PublicanRoot(APIView):
    """
    Find all publican entities and return them as hyperlinked resources.
    """
    def get(self, request, *args, **kwargs):
        app_label = api_utils.get_app_label()
        entity_models = {model._meta.verbose_name_plural: 
                         model.__bases__[0]._meta.verbose_name 
                         for model in models.get_models() 
                         if model._meta.app_label == app_label}
        entity_models = OrderedDict(sorted(entity_models.items(), key=itemgetter(1, 0)))
        for verbose_name_plural, base_model_name in entity_models.items():
            try:
                entity_models[verbose_name_plural] = reverse(
                    base_model_name + "_list_create", 
                    kwargs={base_model_name: verbose_name_plural}, 
                    request=request, 
                    format=kwargs.get('format', None)
                )
            except NoReverseMatch:
                continue
        try:
            entity_models['users'] = reverse('user_list_create', 
                                             request=request, 
                                             format=kwargs.get('format', None)
                                             )
        except NoReverseMatch:
            pass

        return Response(entity_models)
# /PublicanRoot


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
        drink = self.kwargs.get('drink', None)
        drink_model = get_model_by_slug(drink)
        try:
            return drink_model.objects.all()
        except drink_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        drink = self.kwargs.get('drink', None)
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
    def get_object(self):
        drink = self.kwargs.get('drink', None)
        drink_id = self.kwargs.get('drink_id', None)
        drink_model = get_model_by_slug(drink)
        try:
            return drink_model.objects.get(pk=drink_id)
        except drink_model.DoesNotExist:
            raise Http404
        except ValueError:
            try:
                return drink_model.objects.get(slug=drink_id)
            except drink_model.DoesNotExist:
                raise Http404
            
    def get_serializer_class(self):
        drink = self.kwargs.get('drink', None)
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
        facility = self.kwargs.get('facility', None)
        facility_model = get_model_by_slug(facility)
        try:
            return facility_model.objects.all()
        except facility_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        facility = self.kwargs.get('facility', None)
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
    def get_object(self):
        facility = self.kwargs.get('facility', None)
        facility_id = self.kwargs.get('facility_id', None)
        facility_model = get_model_by_slug(facility)
        try:
            return facility_model.objects.get(pk=facility_id)
        except facility_model.DoesNotExist:
            raise Http404
        except ValueError:
            try:
                return facility_model.objects.get(slug=facility_id)
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
        glass = self.kwargs.get('glass', None)
        glass_model = get_model_by_slug(glass)
        try:
            return glass_model.objects.all()
        except glass_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        glass = self.kwargs.get('glass', None)
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
    def get_object(self):
        glass = self.kwargs.get('glass', None)
        glass_id = self.kwargs.get('glass_id', None)
        glass_model = get_model_by_slug(glass)
        try:
            return glass_model.objects.get(pk=glass_id)
        except glass_model.DoesNotExist:
            raise Http404
        except ValueError:
            try:
                return glass_model.objects.get(slug=glass_id)
            except glass_model.DoesNotExist:
                raise Http404
    
    def get_serializer_class(self):
        glass = self.kwargs.get('glass', None)
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
        style = self.kwargs.get('style', None)
        style_model = get_model_by_slug(style)
        try:
            return style_model.objects.all()
        except style_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        style = self.kwargs.get('style', None)
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
    def get_object(self):
        style = self.kwargs.get('style', None)
        style_id = self.kwargs.get('style_id', None)
        style_model = get_model_by_slug(style)
        try:
            return style_model.objects.get(pk=style_id)
        except style_model.DoesNotExist:
            raise Http404
        except ValueError:
            try:
                return style_model.objects.get(slug=style_id)
            except style_model.DoesNotExist:
                raise Http404
    
    def get_serializer_class(self):
        style = self.kwargs.get('style', None)
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
        review = self.kwargs.get('review', None)
        review_model = get_model_by_slug(review)
        try:
            return review_model.objects.all()
        except review_model.DoesNotExist:
            raise Http404
    
    def get_serializer_class(self):
        review = self.kwargs.get('review', None)
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
    def get_object(self):
        review = self.kwargs.get('review', None)
        review_id = self.kwargs.get('review_id', None)
        review_model = get_model_by_slug(review)
        try:
            review = review_model.objects.get(pk=style_id)
        except review_model.DoesNotExist:
            raise Http404
        except ValueError:
            try:
                review = review_model.objects.get(slug=style_id)
            except review_model.DoesNotExist:
                raise Http404
        self.check_object_permissions(self.request, review)
        return(review)
    
    def get_serializer_class(self):
        review = self.kwargs.get('review', None)
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
    def get_object(self):
        user_id = self.kwargs.get('user_id', None)
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404
        except ValueError:
            try:
                return User.objects.get(username=user_id)
            except User.DoesNotExist:
                raise Http404
    
    serializer_class = api_serializers.UserSerializer
# /UserRetrieveUpdateDestroy


class FavoriteList(APIView):
    """
    """
    
    def get_user(self, user_id=None):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404
        except ValueError:
            try:
                return User.objects.get(username=user_id)
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
            entity_models = [models.get_model(app_label, model.__name__) 
                             for model in models.get_models(include_auto_created=True) 
                             if issubclass(model, api_basemodels.Favorite)]
            serialized_items = OrderedDict()
            for entity_model in entity_models:
                publican_items = entity_model.objects.filter(favorite_of=publican_user)
                entity_slug = entity_model._meta.verbose_name_plural
                item_serializer = self.get_serializer(entity_slug)
                serializer = item_serializer(publican_items, many=True)
                serialized_items[entity_slug] = serializer.data
                serialized_items = OrderedDict(sorted(serialized_items.items(), 
                                               key=itemgetter(0)))
        
        return Response(serialized_items)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# /FavoriteList


class FavoriteDetail(APIView):
    """
    """
    
    def get_object(self, entity=None, entity_id=None):
        entity_model = get_model_by_slug(entity)
        try:
            return entity_model.objects.get(pk=entity_id)
        except entity_model.DoesNotExist:
            raise Http404
        except ValueError:
            try:
                return entity_model.objects.get(entity_id)
            except entity_model.DoesNotExist:
                raise Http404
    
    def get_user(self, user_id=None):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404
        except ValueError:
            try:
                return User.objects.get(username=user_id)
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
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404
        except ValueError:
            try:
                return User.objects.get(slug=user_id)
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
            item = entity_model.objects.get(pk=entity_id)
        except entity_model.DoesNotExist:
            raise Http404
        except ValueError:
            try:
                item = entity_model.objects.get(entity_id)
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
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404
        except ValueError:
            try:
                return User.objects.get(slug=user_id)
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