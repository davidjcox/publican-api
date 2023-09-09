"""publican_api views"""

from django.http import Http404
from django.db.models import Q
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from publican_api import models as api_models
from publican_api import serializers as api_serializers 


class DrinkListView(generics.ListAPIView):
    """
    List beers, wines, or liquors.
    Drink type is determined by drink parameter.
    No throttling.
    Permit anonymous and authenticated users to list drinks.
    """
    def get_queryset(self):
        querysets = {'beer':api_models.Beer.objects.all(), 
                     'wine':api_models.Wine.objects.all(), 
                     'liquor':api_models.Liquor.objects.all()}
        return querysets[self.kwargs['drink']]
    
    def get_serializer_class(self):
        serializers = {'beer':api_serializers.BeerSerializer, 
                       'wine':api_serializers.WineSerializer, 
                       'liquor':api_serializers.LiquorSerializer}
        return serializers[self.kwargs['drink']]
    
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
        serializers = {'beer':api_serializers.BeerSerializer, 
                       'wine':api_serializers.WineSerializer, 
                       'liquor':api_serializers.LiquorSerializer}
        return serializers[self.kwargs['drink']]
    
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
        id = self.kwargs['id']
        querysets = {'beer':api_models.Beer.objects.filter(Q(slug=id) | Q(pk=id)), 
                     'wine':api_models.Wine.objects.filter(Q(slug=id) | Q(pk=id)), 
                     'liquor':api_models.Liquor.objects.filter(Q(slug=id) | Q(pk=id))}
        return querysets[self.kwargs['drink']]
    
    def get_serializer_class(self):
        serializers = {'beer':api_serializers.BeerSerializer, 
                       'wine':api_serializers.WineSerializer, 
                       'liquor':api_serializers.LiquorSerializer}
        return serializers[self.kwargs['drink']]
    
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
        querysets = {'beer':api_models.Brewery.objects.all(), 
                     'wine':api_models.Winery.objects.all(), 
                     'liquor':api_models.Distillery.objects.all()}
        return querysets[self.kwargs['drink']]
    
    def get_serializer_class(self):
        serializers = {'beer':api_serializers.BrewerySerializer, 
                       'wine':api_serializers.WinerySerializer, 
                       'liquor':api_serializers.DistillerySerializer}
        return serializers[self.kwargs['drink']]
    
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
        serializers = {'beer':api_serializers.BrewerySerializer, 
                       'wine':api_serializers.WinerySerializer, 
                       'liquor':api_serializers.DistillerySerializer}
        return serializers[self.kwargs['drink']]
    
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
        id = self.kwargs['id']
        querysets = {'beer':api_models.Brewery.objects.filter(Q(slug=id) | Q(pk=id)), 
                     'wine':api_models.Winery.objects.filter(Q(slug=id) | Q(pk=id)), 
                     'liquor':api_models.Distillery.objects.filter(Q(slug=id) | Q(pk=id))}
        return querysets[self.kwargs['drink']]
    
    def get_serializer_class(self):
        serializers = {'beer':api_serializers.BrewerySerializer, 
                       'wine':api_serializers.WinerySerializer, 
                       'liquor':api_serializers.DistillerySerializer}
        return serializers[self.kwargs['drink']]
    
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
        querysets = {'beer':api_models.BeerGlass.objects.all(), 
                     'wine':api_models.WineGlass.objects.all(), 
                     'liquor':api_models.LiquorGlass.objects.all()}
        return querysets[self.kwargs['drink']]
    
    def get_serializer_class(self):
        serializers = {'beer':api_serializers.BeerGlassSerializer, 
                       'wine':api_serializers.WineGlassSerializer, 
                       'liquor':api_serializers.LiquorGlassSerializer}
        return serializers[self.kwargs['drink']]
    
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
        serializers = {'beer':api_serializers.BeerGlassSerializer, 
                       'wine':api_serializers.WineGlassSerializer, 
                       'liquor':api_serializers.LiquorGlassSerializer}
        return serializers[self.kwargs['drink']]
    
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
        id = self.kwargs['id']
        querysets = {'beer':api_models.BeerGlass.objects.filter(Q(slug=id) | Q(pk=id)), 
                     'wine':api_models.WineGlass.objects.filter(Q(slug=id) | Q(pk=id)), 
                     'liquor':api_models.LiquorGlass.objects.filter(Q(slug=id) | Q(pk=id))}
        return querysets[self.kwargs['drink']]
    
    def get_serializer_class(self):
        serializers = {'beer':api_serializers.BeerGlassSerializer, 
                       'wine':api_serializers.WineGlassSerializer, 
                       'liquor':api_serializers.LiquorGlassSerializer}
        return serializers[self.kwargs['drink']]
    
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
        querysets = {'beer':api_models.BeerStyle.objects.all(), 
                     'wine':api_models.WineStyle.objects.all(), 
                     'liquor':api_models.LiquorStyle.objects.all()}
        return querysets[self.kwargs['drink']]
    
    def get_serializer_class(self):
        serializers = {'beer':api_serializers.BeerStyleSerializer, 
                       'wine':api_serializers.WineStyleSerializer, 
                       'liquor':api_serializers.LiquorStyleSerializer}
        return serializers[self.kwargs['drink']]
    
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
        serializers = {'beer':api_serializers.BeerStyleSerializer, 
                       'wine':api_serializers.WineStyleSerializer, 
                       'liquor':api_serializers.LiquorStyleSerializer}
        return serializers[self.kwargs['drink']]
    
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
        id = self.kwargs['id']
        querysets = {'beer':api_models.BeerStyle.objects.filter(Q(slug=id) | Q(pk=id)), 
                     'wine':api_models.WineStyle.objects.filter(Q(slug=id) | Q(pk=id)), 
                     'liquor':api_models.LiquorStyle.objects.filter(Q(slug=id) | Q(pk=id))}
        return querysets[self.kwargs['drink']]
    
    def get_serializer_class(self):
        serializers = {'beer':api_serializers.BeerStyleSerializer, 
                       'wine':api_serializers.WineStyleSerializer, 
                       'liquor':api_serializers.LiquorStyleSerializer}
        return serializers[self.kwargs['drink']]
    
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
        querysets = {'beer':api_models.BeerReview.objects.all(), 
                     'wine':api_models.WineReview.objects.all(), 
                     'liquor':api_models.LiquorReview.objects.all()}
        return querysets[self.kwargs['drink']]
    
    def get_serializer_class(self):
        serializers = {'beer':api_serializers.BeerReviewSerializer, 
                       'wine':api_serializers.WineReviewSerializer, 
                       'liquor':api_serializers.LiquorReviewSerializer}
        return serializers[self.kwargs['drink']]
    
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
        serializers = {'beer':api_serializers.BeerReviewSerializer, 
                       'wine':api_serializers.WineReviewSerializer, 
                       'liquor':api_serializers.LiquorReviewSerializer}
        return serializers[self.kwargs['drink']]
    
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
        id = self.kwargs['id']
        querysets = {'beer':api_models.Beer.objects.filter(Q(slug=id) | Q(pk=id)), 
                     'wine':api_models.Wine.objects.filter(Q(slug=id) | Q(pk=id)), 
                     'liquor':api_models.Liquor.objects.filter(Q(slug=id) | Q(pk=id))}
        return querysets[self.kwargs['drink']]
    
    def get_serializer_class(self):
        serializers = {'beer':api_serializers.BeerSerializer, 
                       'wine':api_serializers.WineSerializer, 
                       'liquor':api_serializers.LiquorSerializer}
        return serializers[self.kwargs['drink']]
    
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


class UserRetrieveUpdateDestroy(generics.RetrieveAPIView):
    """
    Retrieve, update, or delete a registered user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
# /UserRetrieveUpdateDestroy


@api_view(['POST')
def togglefavorite(request, user=None, item=None):
    querysets = {'beer':api_models.Beer.objects.filter(Q(slug=id) | Q(pk=id)), 
                 'wine':api_models.Wine.objects.filter(Q(slug=id) | Q(pk=id)), 
                 'liquor':api_models.Liquor.objects.filter(Q(slug=id) | Q(pk=id)), 
                 'brewery':api_models.Brewery.objects.filter(Q(slug=id) | Q(pk=id)) , 
                 'winery':api_models.Winery.objects.filter(Q(slug=id) | Q(pk=id)) , 
                 'distillery':api_models.Distillery.objects.filter(Q(slug=id) | Q(pk=id)) , 
                 'beerglass':api_models.BeerGlass.objects.filter(Q(slug=id) | Q(pk=id)), 
                 'wineglass':api_models.WineGlass.objects.filter(Q(slug=id) | Q(pk=id)), 
                 'liquorglass':api_models.LiquorGlass.objects.filter(Q(slug=id) | Q(pk=id)), 
                 'beerstyle':api_models.BeerStyle.objects.filter(Q(slug=id) | Q(pk=id)), 
                 'winestyle':api_models.WineStyle.objects.filter(Q(slug=id) | Q(pk=id)), 
                 'liquorstyle':api_models.LiquorStyle.objects.filter(Q(slug=id) | Q(pk=id)), 
    user = User.objects.get(Q(pk=user) | Q(username=user))
    item = querysets['item'][0]
    if item.favorite_of is not None:
        

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
        id = self.kwargs['id']
        querysets = {'install':api_models.InstallationInstructions.objects.get(Q(slug=id) | Q(pk=id)), 
                     'execute':api_models.ExecutionInstructions.objects.get(Q(slug=id) | Q(pk=id)), 
                     'require':api_models.APIRequirements.objects.get(Q(slug=id) | Q(pk=id)), 
                     'define':api_models.APIDefinition.objects.get(Q(slug=id) | Q(pk=id)), 
                     'basemodels':api_models.APIBaseModels.objects.get(Q(slug=id) | Q(pk=id)), 
                     'models':api_models.APIModels.objects.get(Q(slug=id) | Q(pk=id)), 
                     'views':api_models.APIViews.objects.get(Q(slug=id) | Q(pk=id)), 
                     'serializers':api_models.APISerializers.objects.get(Q(slug=id) | Q(pk=id)), 
                     'throttles':api_models.APIThrottles.objects.get(Q(slug=id) | Q(pk=id)), 
                     'permissions':api_models.APIPermissions.objects.get(Q(slug=id) | Q(pk=id))}
        return querysets[self.kwargs['document']]
    
    def get_serializer_class(self):
        serializers = {'install':api_serializers.InstallationInstructionsSerializer, 
                       'execute':api_serializers.ExecutionInstructionsSerializer, 
                       'require':api_serializers.APIRequirementsSerializer, 
                       'define':api_serializers.APIDefinitionSerializer, 
                       'basemodels':api_serializers.APIBaseModelsSerializer, 
                       'models':api_serializers.APIModelsSerializer, 
                       'views':api_serializers.APIViewsSerializer, 
                       'serializers':api_serializers.APISerializersSerializer, 
                       'throttles':api_serializers.APIThrottlesSerializer, 
                       'permissions':api_serializers.APIPermissionsSerializer}
        return serializers[self.kwargs['document']]
    
    permission_classes = (IsAuthenticated,)
# /DocumentRetrieveView

                     
# EOF - publican_api views