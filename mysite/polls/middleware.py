from django.http import Http404
from django.utils.deprecation import MiddlewareMixin
import requests
from django.conf import settings
# class JSONTranslationMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.translations = {
#             "en": {"greeting": "Hello", "header": "Welcome Django!"},
#             "nl": {"greeting": "Hallo", "header": "Welkom Django!"},
#         }
#
#     def __call__(self, request):
#         response = self.get_response(request)
#         return response
#
#     def process_template_response(self, request, response):
#         if "nl" in request.META["HTTP_ACCEPT_LANGUAGE"]:
#             response.context_data["translations"] = self.translations
#             return response
#         return response

class FilterIPMiddleware(MiddlewareMixin):
    # Check if client IP is allowed
    def process_request(self, request):
        allowed_ips = ['192.168.1.1', '123.123.123.123','127.0.0.1'] # Authorized ip's
        ip = request.META.get('REMOTE_ADDR') # Get client IP
        print(ip)
        if ip not in allowed_ips:
            raise Http404 # If user is not allowed raise Error
           #print('Your IP is '+ip)

       # If IP is allowed we don't do anything
        return None

# class StackOverflowMiddleware(MiddlewareMixin):
#     def process_exception(self, request, exception):
#         if settings.DEBUG:
#             intitle = u'{}: {}'.format(exception.__class__.__name__,  exception.message)
#             print (intitle)
#
#             url = 'https://api.stackexchange.com/2.2/search'
#             headers = { 'User-Agent': 'github.com/vitorfs/seot' }
#             params = {
#                 'order': 'desc',
#                 'sort': 'votes',
#                 'site': 'stackoverflow',
#                 'pagesize': 3,
#                 'tagged': 'python;django',
#                 'intitle': intitle
#             }
#
#             r = requests.get(url, params=params, headers=headers)
#             questions = r.json()
#
#             print ('')
#
#             for question in questions['items']:
#                 print (question['title'])
#                 print (question['link'])
#                 print ('')
#
#         return None