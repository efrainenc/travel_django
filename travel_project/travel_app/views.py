from django.shortcuts import render

from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView


#adds location class for mock database data
class Location:
  def __init__(self, country, city, bio):
    self.country = country
    self.city = city
    self.bio = bio

locations = [
  
]

#adds spot class for mock database data
class Spot():
  def __init__(self, name, activity, image):
    self.name = name
    self.activity = activity
    self.image = image

spots = [
 
]

# Create your views here.
class Home(TemplateView):
  template_name = 'home.html'

class About(TemplateView):
  template_name = 'about.html'

class LocationList(TemplateView):
  template_name = "location_list.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["locations"] = locations # this is where we add the key into our context object for the view to use
    return context

class SpotList(TemplateView):
  template_name = "spot_list.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["spots"] = spots # this is where we add the key into our context object for the view to use
    return context

