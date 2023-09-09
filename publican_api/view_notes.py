

facility_patterns = patterns('', 
    url(r'^/$', views.?, name='?'), 
    url(r'^/(?P<facility_pk>[0-9]+)/$', views.?, name='?'), 
    url(r'^(/(?P<facility_slug>\b[a-z0-9\-]+\b)/$', views.?, name='?'), 
)

    url(r'^(?P<facility>(brewery|winery|distillery))', include(facility_patterns)), 
    url(r'^(?P<drink>(beer|wine|liquor))/(?P<facility>(brewery|winery|distillery))', include(facility_patterns)), 
    url(r'^(?P<drink>(beer|wine|liquor))/(?P<drink_pk>[0-9]+)/(?P<facility>(brewery|winery|distillery))', include(facility_patterns)), 
    url(r'^(?P<drink>(beer|wine|liquor))/(?P<drink_slug>\b[a-z0-9\-]+\b)/(?P<facility>(brewery|winery|distillery))', include(facility_patterns)), 
    
    <facility>                                      LIST
    <drink> <facility>                              LIST
    <drink> <drink_pk> <facility>                   LIST
    <drink> <drink_slug> <facility>                 LIST
    
    def get_queryset(self):
        d_pk = self.kwargs['drink_pk']
        d_slug = self.kwargs['drink_slug']
    
    
    <facility> <facility_pk>                        RETRIEVE
    <facility> <facility_slug>                      RETRIEVE
    <drink> <facility> <facility_pk>                RETRIEVE
    <drink> <facility> <facility_slug>              RETRIEVE
    <drink> <drink_pk> <facility> <facility_pk>     RETRIEVE
    <drink> <drink_pk> <facility> <facility_slug>   RETRIEVE
    <drink> <drink_slug> <facility> <facility_pk>   RETRIEVE
    <drink> <drink_slug> <facility> <facility_slug> RETRIEVE
    
	def get_queryset(self):
        facility = self.kwargs['facility']
        f_pk = self.kwargs['facility_pk']
        f_slug = self.kwargs['facility_slug']
        drink = self.kwargs['drink']
        d_pk = self.kwargs['drink_pk']
        d_slug = self.kwargs['drink_slug']
        
        if bool(drink):
            if bool(f_pk) ^ bool(f_slug):
                if bool(d_pk) ^ bool(d_slug):
                    querysets = {'beer':api_models.Brewery.objects.filter(
                                                Q(pk=f_pk) | Q(slug=f_slug)
                                            ).filter(
                                                Q(beer__pk=d_pk ) | Q(beer__slug=d_slug)
                                            ), 
                                 'wine':api_models.Winery.objects.filter(
                                                Q(pk=f_pk) | Q(slug=f_slug)
                                            ).filter(
                                                Q(wine__pk=d_pk ) | Q(wine__slug=d_slug)
                                            ), 
                                 'liquor':api_models.Distillery.objects.filter(
                                                Q(pk=f_pk) | Q(slug=f_slug)
                                            ).filter(
                                                Q(liquor__pk=d_pk ) | Q(liquor__slug=d_slug)
                                            )
                                }
                else:
                    querysets = {'beer':api_models.Brewery.objects.filter(
                                                Q(pk=f_pk) | Q(slug=f_slug)
                                            ), 
                                 'wine':api_models.Winery.objects.filter(
                                                Q(pk=f_pk) | Q(slug=f_slug)
                                            ), 
                                 'liquor':api_models.Distillery.objects.filter(
                                                Q(pk=f_pk) | Q(slug=f_slug)
                                            )
                                }
            return querysets[self.kwargs['drink']]
        elif bool(facility):
            querysets = {'brewery':api_models.Brewery.objects.get(
                                            Q(pk=f_pk) | Q(slug=f_slug)
                                        )
                         'winery':api_models.Winery.objects.get(
                                            Q(pk=f_pk) | Q(slug=f_slug)
                                        )
                         'distillery':api_models.Distillery.objects.get(
                                            Q(pk=f_pk) | Q(slug=f_slug)
                                        )
                        }
            return querysets[self.kwargs['facility']]
    #/get_queryset