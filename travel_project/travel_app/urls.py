from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('about/', views.About.as_view(), name="about"),
    path('locations/', views.LocationList.as_view(), name="location_list"),
    path('location/<int:pk>/spots', views.SpotDisplay.as_view(), name="spot_list"),
    path('spots/', views.SpotList.as_view(), name="spot_list"),
    path('spots/new/', views.SpotCreate.as_view(), name="spot_create"),
    path('spots/<int:pk>', views.SpotDetail.as_view(), name="spot_detail"),
    path('spots/<int:pk>/update',views.SpotUpdate.as_view(), name="spot_update"),
    path('spots/<int:pk>/delete',views.SpotDelete.as_view(), name="spot_delete"),
]
