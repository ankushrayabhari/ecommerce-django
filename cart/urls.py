from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^remove/(?P<id>[0-9]+)$', views.remove, name="remove"),
    url(r'^add/(?P<id>[0-9]+)$', views.addToCart, name="add"),
    url(r'^update/(?P<id>[0-9]+)$', views.update, name="update"),
]