from django.urls import path
from django.contrib import admin
from django.conf import settings    
from fire.views import (
    HomePageView, 
    ChartView, 
    PieCountbySeverity, 
    LineCountbyMonth,
    MultilineIncidentTop3Country, 
    multipleBarbySeverity, 
    map_station,
    fire_incident_map,
    # Remove dashboard_chart if you're not using it
    FireStationListView,
    FireStationCreateView,
    FireStationUpdateView,
    FireStationDeleteView,
    IncidentListView, 
    IncidentCreateView, 
    IncidentUpdateView,
    IncidentDeleteView,
    LocationListView, 
    LocationCreateView, 
    LocationUpdateView,
    LocationDeleteView,
    ConditionListView, 
    ConditionCreateView, 
    ConditionUpdateView,
    ConditionDeleteView,
    FiretruckListView, 
    FiretruckCreateView, 
    FiretruckUpdateView,
    FiretruckDeleteView,
    FirefightersListView, 
    FirefightersCreateView, 
    FirefightersUpdateView,
    FirefightersDeleteView,
    BoatListView, 
    BoatCreateView, 
    BoatUpdateView
)

urlpatterns = [
    # Main views
        path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard-chart', ChartView.as_view(), name='dashboard-chart'),
    


    # Chart data APIs
    path('chart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),
    
    
    # Map views
    path('stations/', map_station, name='map-station'), 
    path('fire_incident_map/', fire_incident_map, name='fire_incidents_map'),
    
    # Fire Station URLs
    path('station/', FireStationListView.as_view(), name='station-list'),
    path('station/add/', FireStationCreateView.as_view(), name='station-add'),
    path('station/<int:pk>/edit/', FireStationUpdateView.as_view(), name='station-update'),
    path('station/<int:pk>/delete/', FireStationDeleteView.as_view(), name='station-delete'),
    
    # Incident URLs
    path('incidents/', IncidentListView.as_view(), name='incident-list'),
    path('incident/create/', IncidentCreateView.as_view(), name='incident-add'),
    path('incident/<int:pk>/update/', IncidentUpdateView.as_view(), name='incident-update'),
    path('incident_list/<pk>/delete/', IncidentDeleteView.as_view(), name='incident-delete'),
    
    # Location URLs
    path('locations/', LocationListView.as_view(), name='loc-list'),
    path('location/create/', LocationCreateView.as_view(), name='location-add'),
    path('location/<int:pk>/update/', LocationUpdateView.as_view(), name='location-update'),
    path('location_list/<pk>/delete/', LocationDeleteView.as_view(), name='location-delete'),
    
    # Weather Condition URLs
    path('weather/', ConditionListView.as_view(), name='weather-list'),
    path('weather/create/', ConditionCreateView.as_view(), name='weather_add'),
    path('weather/<int:pk>/update/', ConditionUpdateView.as_view(), name='weather-update'),
    path('weather/<int:pk>/delete/', ConditionDeleteView.as_view(), name='weather-delete'),
    
    
    # Firetruck URLs
    path('firetrucks/', FiretruckListView.as_view(), name='fireTruck-list'),
    path('firetruck/create/', FiretruckCreateView.as_view(), name='firetruck-add'),
    path('firetruck/<int:pk>/update/', FiretruckUpdateView.as_view(), name='firetruck-update'),
    path('firetruck_list/<pk>/delete/', FiretruckDeleteView.as_view(), name='firetruck-delete'),
    
    # Firefighters URLs
    path('firefighters/', FirefightersListView.as_view(), name='firefighters-list'),
    path('firefighter/create/', FirefightersCreateView.as_view(), name='firefighters-add'),
    path('firefighter/<int:pk>/update/', FirefightersUpdateView.as_view(), name='firefighters-update'),
    path('firefighters/<int:pk>/delete/', FirefightersDeleteView.as_view(), name='firefighters-delete'),
    
    # Condition URLs
    path('condition_list/',  ConditionListView.as_view(), name='weather-list'),
    path('condition_list/add', ConditionCreateView.as_view(), name='condition-add'),
    path('condition_list/<pk>', ConditionUpdateView.as_view(), name='condition-update'),
    path('condition_list/<pk>/delete/', ConditionDeleteView.as_view(), name='condition-delete'),
    
    # Boat URLs
    path('boats/', BoatListView.as_view(), name='boat_list'),
    path('boat/create/', BoatCreateView.as_view(), name='boat_add'),
    path('boat/<int:pk>/update/', BoatUpdateView.as_view(), name='boat_update'),
]