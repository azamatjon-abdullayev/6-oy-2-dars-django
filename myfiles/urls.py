from django.urls import path
from .views import *
urlpatterns = [
    path('',home),
    path('iron/',iron_man),
    path('3-view/', view3),
    path('4-view/', view4),
    path('5-view/', view5),
    path('6-view/', view6),
    path('7-view/', view7),
    path('8-view/', view8),
    path('9-view/', view9),
    path('10-view/', view10),
]