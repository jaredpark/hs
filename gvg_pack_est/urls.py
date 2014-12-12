from django.conf.urls import patterns, url
# import completed views
from gvg_pack_est import views
# r'^$' matches the empty string - so any reference to the root url
# when it is matched, reference index() in views.py and give it name 'index'
urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	url(r'^estimate/', views.estimate, name = 'estimate'),
	url(r'^test_page/', views.test_page, name = 'test_page'),
#	url(r'^about/', views.about, name = 'about'),
	)