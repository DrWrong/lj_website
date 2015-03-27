from django.conf.urls import patterns, url
from solutions import views


urlpatterns = patterns(
    '',
    url(r'^$', views.SolutionListView.as_view(), name="solutionindex"),
    url(r'(?P<pk>\d+)$', views.SolutionDetailView.as_view(),
        name="solutiondetail"),
)
