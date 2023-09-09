"""publican_api throttles"""

from rest_framework import throttling


SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class BurstRateThrottle(throttling.UserRateThrottle):
    scope = 'burst'

    
class SustainedRateThrottle(throttling.UserRateThrottle):
    scope = 'sustained'

    
class CustomListCreateThrottle(throttling.ScopedRateThrottle):
    """
    Subclass DRF 'ScopedRateThrottle' and override 'allow_request' so that any 
    request.merthod == 'POST' will be throttled as usual but any 
    request.method == 'GET' will not be throttled at all.  Had to do this to 
    allow throttling to be applied to 'ListCreate' views selectively.
    """
    def parse_rate(self, rate):
        """
        Override SimpleRateThrottle method to add week ('w') to 'duration'.
        """
        if rate is None:
            return (None, None)
        num, period = rate.split('/')
        num_requests = int(num)
        duration = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400, 'w': 604800}[period[0]]
        return (num_requests, duration)
    
    def allow_request(self, request, view):
        # We can only determine the scope once we're called by the view.
        self.scope = getattr(view, self.scope_attr, None)
        
        # If the request method is read-only always allow the request.
        if request.method in SAFE_METHODS:
            return True
        
        # If a view does not have a `throttle_scope` always allow the request
        if not self.scope:
            return True
        
        # Determine the allowed request rate as we normally would during
        # the `__init__` call.
        self.rate = self.get_rate()
        self.num_requests, self.duration = self.parse_rate(self.rate)
        
        # We can now proceed as normal.
        return super(throttling.ScopedRateThrottle, self).allow_request(request, view)
# /CustomListCreateThrottle


# EOF - publican_api throttles