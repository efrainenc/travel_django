from django.shortcuts import render

from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView


#adds location class for mock database data
class Location:
  def __init__(self, country, city, image):
    self.country = country
    self.city = city
    self.image = image

locations = [
  Location('France', 'Paris', 'https://images.adsttc.com/media/images/5d44/14fa/284d/d1fd/3a00/003d/large_jpg/eiffel-tower-in-paris-151-medium.jpg?1564742900'),
  Location('Hawaii', 'Maui', 'https://www.lovebigisland.com/wp-content/uploads/hana-highway.jpg'),
  Location('South Island', 'New Zealand', 'https://img.traveltriangle.com/blog/wp-content/uploads/2018/12/new-zealand-south-island-booking-cover.jpg'),
  Location('French Polynesia', 'Bora Bora', 'https://tahititourisme.com/wp-content/uploads/2020/02/whereisborabora.jpg'),
  Location('Italy', 'Rome', 'https://fullsuitcase.com/wp-content/uploads/2022/01/Best-views-and-viewpoints-in-Rome-Italy.jpg.webp'),
  Location('Japan', 'Tokyo', 'https://media.istockphoto.com/id/1131743616/photo/aerial-view-of-tokyo-cityscape-with-fuji-mountain-in-japan.jpg?s=612x612&w=0&k=20&c=0QcSwnyzP__YpBewnQ6_-OZkn0XDtq-mXyvLSSakjZE='),
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

