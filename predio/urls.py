from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^predios/', views.insert_predio),
    url(r'^propietario/', views.insert_propietario),
    url(r'^propietario/nuevo', views.insertar_propietario, name='insertar_propietario'),
    url(r'^predio/nuevo', views.insertar_predio, name='insertar_predio'),
]