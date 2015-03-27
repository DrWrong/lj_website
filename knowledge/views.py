from django.views.generic import ListView, DetailView
from .models import Knowledge


class KnowledgeListView(ListView):
    model = Knowledge
    template_name = "knowledgeindex.html"


class KnowledgeDetailView(DetailView):
    model = Knowledge
    template_name = "knowledgedetail.html"
