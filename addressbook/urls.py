from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='home'),
    url(r'^login/$', views.user_login, name="login"),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.register, name='signup'),
    url(r'^mainpage/$', views.mainpage, name='mainpage'),
    url(r'^create/$', views.create, name="create"),
    url(r'^view/$', views.view_contact, name='view'),
    url(r'^search/$', views.search, name='search'),
    url(r'^deletecontact/(?P<userid>\d+)/$', views.deletecontact, name='delete'),
]
