from django.conf.urls import patterns, url
from sidemenu import views


urlpatterns = patterns(
    '',
    url(r'^$', views.ProductIndexView.as_view(), name='app_main'),
    url(r'/(?P<slug>\w+)$', views.ProductDetailView.as_view(),
        name='productdetail'),
)
