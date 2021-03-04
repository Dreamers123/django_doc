from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Musician,Person
from .forms import ContactForm
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.template.response import TemplateResponse
from django.shortcuts import render

class PersonCreate(CreateView):
    model = Person
    fields = ['name']
    #template_name = 'polls/contact.html'

class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('person-list')

class ContactView(FormView):
    template_name = 'polls/contact.html'
    form_class = ContactForm
    success_url = '/1/amp'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

class PersonUpdate(UpdateView):
    model = Person
    fields = ['name']
    template_name_suffix = '_update_form'

class MusicianDetailView(DetailView):

    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    template_name = 'polls/musician_detail.html'
class PersonListView(ListView):

    model = Person
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    template_name = 'polls/person_list.html'
def index(request):
    context = {
        "first_name": "Anjaneyulu",
        "last_name": "Batta",
        "address": "Hyderabad, India"
    }
    #return TemplateResponse(request, "polls/index.html", context)

    return render(request, "polls/index.html", context)
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

@api_view(['POST'])
def api_post(request):
    if request.method == "POST":
            url = 'http://jsonplaceholder.typicode.com/users/'
            payload = {'name':'Abeer'}
            response = requests.post(url, data = payload)
            return Response(response.json(), status=status.HTTP_200_OK)

    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)
def permission_denied_view(request):
    raise PermissionDenied
def response_error_handler(request, exception=None):
    return HttpResponse('Error handler content', status=403)