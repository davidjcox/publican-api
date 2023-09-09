import publican_api.basemodels as api_basemodels
import publican_api.models as api_models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
import publican_api.utils as api_utils

beer1 = api_models.Beer.objects.create(name="beer1", ibu=50, calories=150, abv=0.40)
beer2 = api_models.Beer.objects.create(name="beer2", ibu=50, calories=150, abv=0.40)
beer3 = api_models.Beer.objects.create(name="beer3", ibu=50, calories=150, abv=0.40)
wine1 = api_models.Wine.objects.create(name="wine1", sweetness=400, acidity=0.25, tannin='Low', fruit="fruity")
wine2 = api_models.Wine.objects.create(name="wine2", sweetness=400, acidity=0.25, tannin='Low', fruit="fruity")
wine3 = api_models.Wine.objects.create(name="wine3", sweetness=400, acidity=0.25, tannin='Low', fruit="fruity")
liquor1 = api_models.Liquor.objects.create(name="liquor1", calories=80, abv=50)
liquor2 = api_models.Liquor.objects.create(name="liquor2", calories=80, abv=50)
liquor3 = api_models.Liquor.objects.create(name="liquor3", calories=80, abv=50)
brewery1 = api_models.Brewery.objects.create(name="brewery1", beer=beer1)
brewery2 = api_models.Brewery.objects.create(name="brewery2", beer=beer2)
brewery3 = api_models.Brewery.objects.create(name="brewery3", beer=beer3)
winery1 = api_models.Winery.objects.create(name="winery1", wine=wine1)
winery2 = api_models.Winery.objects.create(name="winery2", wine=wine2)
winery3 = api_models.Winery.objects.create(name="winery3", wine=wine1)
distillery1 = api_models.Distillery.objects.create(name="distillery1", liquor=liquor1)
distillery2 = api_models.Distillery.objects.create(name="distillery2", liquor=liquor2)
distillery3 = api_models.Distillery.objects.create(name="distillery3", liquor=liquor3)
bglass1 = api_models.BeerGlass.objects.create(name="beer glass 1", beer=beer3)
bglass2 = api_models.BeerGlass.objects.create(name="beer glass 2", beer=beer2)
bglass3 = api_models.BeerGlass.objects.create(name="beer glass 3", beer=beer1)
wglass1 = api_models.WineGlass.objects.create(name="wine glass 1", wine=wine1)
wglass2 = api_models.WineGlass.objects.create(name="wine glass 2", wine=wine3)
wglass3 = api_models.WineGlass.objects.create(name="wine glass 3", wine=wine2)
lglass1 = api_models.LiquorGlass.objects.create(name="liquor glass 1", liquor=liquor3)
lglass2 = api_models.LiquorGlass.objects.create(name="liquor glass 2", liquor=liquor1)
lglass3 = api_models.LiquorGlass.objects.create(name="liquor glass 3", liquor=liquor2)
bstyle1 = api_models.BeerStyle.objects.create(name="beer style 1", beer=beer2)
bstyle2 = api_models.BeerStyle.objects.create(name="beer style 2", beer=beer3)
bstyle3 = api_models.BeerStyle.objects.create(name="beer style 3", beer=beer1)
wstyle1 = api_models.WineStyle.objects.update(name="wine style 1", wine=wine1)
wstyle2 = api_models.WineStyle.objects.update(name="wine style 2", wine=wine2)
wstyle3 = api_models.WineStyle.objects.update(name="wine style 3", wine=wine1)
lstyle1 = api_models.LiquorStyle.objects.create(name="liquor style 1", liquor=liquor1)
lstyle2 = api_models.LiquorStyle.objects.create(name="liquor style 2", liquor=liquor3)
lstyle3 = api_models.LiquorStyle.objects.create(name="liquor style 3", liquor=liquor2)
user1 = User.objects.create_user(username="user1", email="user@email.com", password="password1")
user2 = User.objects.create_user(username="user2", email="user@email.com", password="password2")
user3 = User.objects.create_user(username="user3", email="user@email.com", password="password3")

user1 = User.objects.get(username="user1")
user2 = User.objects.get(username="user2")
beer1 = api_models.Beer.objects.get(name="beer1")
wine1 = api_models.Wine.objects.get(name="wine1")

beerreview1 = api_models.BeerReview.objects.create(beer=beer1, rater=user1, title="Good to last drop", description="Tasty, tasty, tasty", appearance=4, aroma=5, taste=4, palate=5, bottlestyle=2)
winereview1 = api_models.WineReview.objects.create(wine=wine1, rater=user2, title="Grapes of wrath", description="Sharp on the finish", clarity=4, color=5, intensity=4, aroma=7, body=3, astringency=5, alcohol=2, balance=2, finish=1, complexity=3, bottlestyle=2)


fav_models = [models.get_model(app_label='publican_api', model_name=model.__name__) 
              for model in models.get_models(app_mod=api_models) 
              if issubclass(model, api_basemodels.Resource)]

              
