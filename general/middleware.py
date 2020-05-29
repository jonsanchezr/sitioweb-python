class ActivateBrowserCacheMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Cache-Control'] = 'public, max-age=43200, immutable'
        response['Expires'] = '43200'
        return response
