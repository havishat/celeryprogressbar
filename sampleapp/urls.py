from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('senddata', views.mycelerytask),
    path('taskstatus', views.mytaskStatus),
    path('index', views.index2, name='index2'),
    #url(r'^$', views.index2,name='index2'),
    url(r'^poll_state$', views.poll_state,name='poll_state'),
]