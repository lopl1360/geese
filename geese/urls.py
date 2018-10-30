from django.conf.urls import url

from . import views

urlpatterns = [
            url(r'forward/$', views.forward, name='forward'),
            url(r'forward/(?P<id>\w+)/$', views.forward, name='forward'),
            url('', views.index, name='index'),
]
