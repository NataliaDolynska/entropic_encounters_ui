from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html")),
    path('main_mission', views.main_mission, name='main_mission'),
    path('role-selection/', views.role_selection, name='role_selection'),
    path('planet-selection/', views.planet_selection, name='planet_selection'),
    path('planet-description/<str:planet>/', views.planet_description, name='planet_description'),
    path('society-selection/', views.society_selection, name='society_selection'),
    path('society-description/<str:society>/', views.society_description, name='society_description'),
    path('questions-selection/', views.questions_selection, name='questions_selection'),
    path('questions/<str:category>/', views.questions, name='questions_list'),
    path('gameplay/', views.gameplay, name='gameplay'),
    path('reflection-synthesis/', views.reflection_synthesis, name='reflection_synthesis'),
    path('endgame-summary/', views.endgame_summary, name='endgame_summary'),
    path('conditional/<str:condition>/<str:role>/', views.conditional, name='conditional'),
    path('briefing-celestial/<str:society>/<str:planet>/', views.briefing_celestial, name='briefing_celestial'),
    path('briefing-explorer/<str:planet>/<str:society>/', views.briefing_explorer, name='briefing_explorer'),
]
