from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^parameterSet/$', views.parameterSet, name='parameterSet'),
    url(r'^execution/$', views.execution, name='execution'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^submit', views.submit),
    url(r'^download', views.download)

    # url(r'^hello/', 'FastLSH.views.hello'),
    # url(r'^home/', 'FastLSH.views.home'),

]

