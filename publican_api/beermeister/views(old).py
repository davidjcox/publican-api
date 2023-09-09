




class BeerList(APIView):
    """
    List all beers.
    """
    def get(self, request, format=None):
        beers = Beer.objects.all()
        serializer = BeerSerializer(beers, many=True)
        return Response(serializer.data)
# /BeerList

class BeerDetail(APIView):
    """
    Retrieve, update or delete a beer instance.
    """
    def get_object(self, id):
        return Beer.objects.get(Q(slug=id) | Q(pk=id))
    
    def get(self, request, id, format=None):
        beer = self.get_object(id)
        serializer = BeerSerializer(beer)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        beer = self.get_object(id)
        serializer = BeerSerializer(beer, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        beer = self.get_object(id)
        beer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# /BeerDetail


class BeerDetailThrottled(APIView):
    """
    Create a beer.  Throttle beer creations to no more than 1/day.
    """
    throttle_scope = 'drink_creates'
    
    def post(self, request, format=None):
        serializer = BeerSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# /BeerDetailThrottled


class WineList(APIView):
    """
    List all wines.
    """
    def get(self, request, format=None):
        wines = Wine.objects.all()
        serializer = WineSerializer(wines, many=True)
        return Response(serializer.data)
# /WineList


class WineDetail(APIView):
    """
    Retrieve, update or delete a wine instance.
    """
    def get_object(self, id):
        return Wine.objects.get(Q(slug=id) | Q(pk=id))
    
    def get(self, request, id, format=None):
        wine = self.get_object(id)
        serializer = BeerSerializer(wine)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        wine = self.get_object(id)
        serializer = WineSerializer(wine, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        wine = self.get_object(id)
        wine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# /WineDetail


class WineDetailThrottled(APIView):
    """
    Create a wine.  Throttle wine creations to no more than 1/day.
    """
    throttle_scope = 'drink_creates'
    
    def post(self, request, format=None):
        serializer = WineSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# /WineDetailThrottled


class LiquorList(APIView):
    """
    List all liquors.
    """
    def get(self, request, format=None):
        liquors = Liquor.objects.all()
        serializer = LiquorSerializer(liquors, many=True)
        return Response(serializer.data)
# /LiquorList


class LiquorDetail(APIView):
    """
    Retrieve, update or delete a liquor instance.
    """
    def get_object(self, id):
        return Liquor.objects.get(Q(slug=id) | Q(pk=id))
    
    def get(self, request, id, format=None):
        liquor = self.get_object(id)
        serializer = LiquorSerializer(liquor)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        liquor = self.get_object(id)
        serializer = LiquorSerializer(liquor, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        liquor = self.get_object(id)
        liquor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# /LiquorDetail


class LiquorDetailThrottled(APIView):
    """
    Create a liquor.  Throttle liquor creations to < 1/day.
    """
    throttle_scope = 'drink_creates'
    
    def post(self, request, format=None):
        serializer = LiquorSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# /LiquorDetailThrottled


################################################################################