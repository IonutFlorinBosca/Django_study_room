# this will contain the paths for the app base
from django.urls import path
from . import views


# i need to specify a list of urls that the user will go to
urlpatterns = [
    path('', views.home, name="home"),
    # passing on dynamic values - <str:pk> - values type 'string', pk: primary key
    # pass in the pk parameter inside of view
    path('room/<str:pk>', views.room, name="room"),
]
