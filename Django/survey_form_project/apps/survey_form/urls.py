from django.conf.urls import url
from . import views         
urlpatterns = [
    url(r'^$', views.index),
    url(r'^survey$', views.index),
    url(r'^surveys/process$', views.process),  
    url(r'^results$', views.results), 
    url(r'^reset$', views.reset),  
]

