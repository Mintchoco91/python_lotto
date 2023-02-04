from django.conf.urls import url, include
from . import views
from django.urls import path

app_name = 'python_lotto_app'

urlpatterns = [
    path('', views.index, name="index"),
    path('insert', views.insertData, name="insert"),
    path('renew', views.renew, name="renew"),
    path('searchByPeriod', views.searchByPeriod, name="searchByPeriod"),
    path('searchByRound', views.searchByRound, name="searchByRound"),
    path('searchByRecent', views.searchByRecent, name="searchByRecent"),
    path('analyze', views.analyze, name="analyze"),
]
