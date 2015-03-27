from django.conf.urls import patterns, url
from news import views


urlpatterns = patterns(
    '',
    url(r'^$', views.NewsIndexView.as_view(), name="newsindex"),
    url(r'(?P<pk>\d+)$', views.NewsDetailView.as_view(), name="newsdetail")
)
