from django.shortcuts import render

from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
# This will import the class we are extending 
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView
from .forms import SpotForm

# import models
from .models import Location, Spot

# Create your views here.
class Home(TemplateView):
  template_name = 'home.html'

class About(TemplateView):
  template_name = 'about.html'

# Location Views
class LocationList(TemplateView):
    template_name = "location_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        country = self.request.GET.get("country")
        # If a query exists we will filter by name 
        if country != None:
            # .filter is the sql WHERE statement and country__icontains is doing a search for any country that contains the query param
            context["locations"] = Location.objects.filter(country__icontains=country)
        else:
            context["locations"] = Location.objects.all()
        return context

class LocationImageDisplay(DetailView):
    model = Location
    template_name = 'location_list.html'
    context_object_name = 'location'

# Spot Views
class SpotList(TemplateView):
  template_name = "spot_list.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["spots"] = Spot.objects.all()
    return context

class SpotCreate(CreateView):
    model = Spot
    fields = ['location', 'name', 'description', 'address', 'image', 'num_stars']
    template_name = "spot_create.html"
    success_url = "/spots/"

class SpotImage(TemplateView):
    form = SpotForm
    template_name = 'spot_create.html'

    def post(self, request, *args, **kwargs):
        form = SpotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('home', kwargs={'pk': pk}))
        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class SpotImageDisplay(DetailView):
    model = Spot
    template_name = 'spot_list.html'
    context_object_name = 'spot'

class SpotDisplay(DetailView):
    model = Spot
    template_name = 'spot_list.html'