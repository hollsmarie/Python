from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new), 
    url(r'^create$', views.create),  
    url(r'^{{number}}$', views.show),  
    url(r'^{{number}}/edit$', views.edit),  
    url(r'^{{number}}/delete$', views.destroy),     
]

#whatever