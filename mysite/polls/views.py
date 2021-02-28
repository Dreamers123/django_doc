from django.http import HttpResponse
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

def index(request):
    return HttpResponse("<h3 style='color:red;text-align:center'>Hello, world. You're at the polls index.</h3>")
@api_view(('GET',))
#@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def api_index(request):
     url = 'http://jsonplaceholder.typicode.com/users/'
     r = requests.get(url)
     data = r.json()
     return Response(data, status=status.HTTP_200_OK)
@api_view(('GET',))
def api_details(request, id):
    url = 'http://jsonplaceholder.typicode.com/users/' + str(id)
    r = requests.get(url)
    data = r.json()
    return Response(data, status=status.HTTP_200_OK)

# @api_view(['POST'])
# def api_post(request):
#     if request.method == "POST":
#             url = 'http://jsonplaceholder.typicode.com/users/'
#             payload = {'name':'Abeer'}
#             response = requests.post(url, data = payload)
#             return Response(response.json(), status=status.HTTP_200_OK)
#
#     else:
#         return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)
