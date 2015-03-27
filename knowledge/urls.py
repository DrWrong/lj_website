from django.conf.urls import patterns, url
from knowledge import views

urlpatterns = patterns(
    '',
    url(r'^$', views.KnowledgeListView.as_view(), name="knowledgeindex"),
    url(r'(?P<pk>\d+)$', views.KnowledgeDetailView.as_view(),
        name="knowledgedetail"),
)
