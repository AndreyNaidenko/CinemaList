from django.conf.urls import url
from . import views

app_name = 'app_cinema_list'

urlpatterns = [
    url('', views.index, name = "index")
]
