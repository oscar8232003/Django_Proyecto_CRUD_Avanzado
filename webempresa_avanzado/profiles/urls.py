from django.urls import path
from .views import List_Profiles,Detail_Profiles

url_patterns = ([
    path('', List_Profiles.as_view(), name='list'),
    path('<username>/', Detail_Profiles.as_view(), name='detail'),
], "profiles")
