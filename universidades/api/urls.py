from django.conf.urls import include,url
from . import views

urlpatterns = [

    url(r'campus/$', views.CampusView.as_view(), name='Campus_api'),
    url(r'campus/(?P<pk>[0-9]+)/$', views.CampusDetailView.as_view(), name='Campus_detail_api'),

    #contacts urls
	url(r'universidad/$', views.UniversidadView.as_view(), name='Universidad_api'),
	url(r'universidad/(?P<pk>[0-9]+)/$', views.UniversidadDetailView.as_view(), name='Universidad_detail_api'),

]