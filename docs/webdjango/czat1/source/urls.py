from django.urls import path
from docs.webdjango.czat1.source import views

app_name = 'czat'  # przestrzeń nazw aplikacji
urlpatterns = [
    path('', views.index, name='index'),
    path('loguj/', views.loguj, name='loguj'),
    path('wyloguj/', views.wyloguj, name='wyloguj'),
    path('wiadomosci/', views.wiadomosci, name='wiadomosci'),
]