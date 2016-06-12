from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^all/$', views.post_list, name='post_list'),
	url(r'(?P<article_id>^\d+)/$', views.post_single, name='post_single'),
	url(r'^$', views.base, name='base'),
	url(r'(?P<article_id>^\d+)/add_coment/$', views.add_coment, name='add_coment'),
]
