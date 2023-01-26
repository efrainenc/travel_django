from django.shortcuts import render

from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# import models
from .models import Location, Spot

# Create your views here.
class Home(TemplateView):
  template_name = 'home.html'

class About(TemplateView):
  template_name = 'about.html'

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

class SpotList(TemplateView):
  template_name = "spot_list.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["spots"] = Spot.objects.all()
    return context

