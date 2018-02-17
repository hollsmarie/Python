from django.conf.urls import url
from . import views          
  
urlpatterns = [
    url(r'^$', views.index),     
    url(r'^randomword/generate$', views.generate),
    url(r'^randomword/reset$', views.reset)
  ]
