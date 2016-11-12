from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index,name='index'),
    url(r'^form/(?P<bill_id>[0-9]*)$', views.form,name='form'),
    url(r'^add/$', views.add,name='add'),

    url(r'^type/$', views.list_type,name='list_type'),
    url(r'^form/type/(?P<type_id>[0-9]*)$', views.form_type,name='form_type'),
    url(r'^add/type/$', views.add_type,name='add/type'),
]