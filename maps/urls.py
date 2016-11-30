from django.conf.urls import url
from . import views

urlpatterns = [
    # /music
    #url(r'^details/$', views.details, name = 'details'),
     url(r'^$', views.index, name='index'),

    #/musci/111/
    url(r'^(?P<topic_id>[0-9]+)/$', views.details, name = 'details'),
]