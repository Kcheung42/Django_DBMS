from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django_apps.dbms import views

urlpatterns = [
	url(r'^api$', views.ItemMasterList.as_view()),
	url(r'^api/(?P<pk>[0-9]+)/$', views.ItemMasterDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
