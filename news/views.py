from django.views.generic import ListView, DetailView
from news.models import News


class NewsIndexView(ListView):
    model = News
    template_name = "newsindex.html"


class NewsDetailView(DetailView):
    model = News
    template_name = "newsdetail.html"
