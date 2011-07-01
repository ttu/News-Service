from django.conf.urls.defaults import *
 
import views

urlpatterns = patterns('',
	url(r'main/', views.news_main, name='news_main'),
	url(r'^list/', views.news_list, name='news_list'),
	url(r'^hello/', views.hello, name='hello'),
)
