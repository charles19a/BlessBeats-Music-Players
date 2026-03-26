from django.urls import path
from . import views

app_name = 'musicplayer'

urlpatterns = [
    path('', views.player_view, name='player'),
    path('search/', views.search_view, name='search'),
    path('library/', views.library_view, name='library'),
    path('toggle-favorite/<int:song_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('api/search/', views.live_search_api, name='live_search'),
    path('set-timezone/', views.set_timezone, name='set_timezone'),
]
