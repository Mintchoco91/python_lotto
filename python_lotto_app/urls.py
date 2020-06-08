from django.conf.urls import url, include
from . import views
from django.urls import path

app_name = 'python_lotto_app'

urlpatterns = [
    path('', views.selectList),
]
