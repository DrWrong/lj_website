from django.views.generic import ListView, DetailView
from .models import Solution
# Create your views here.


class SolutionListView(ListView):
    model = Solution
    template_name = "solutionindex.html"


class SolutionDetailView(DetailView):
    model = Solution
    template_name = "solutiondetail.html"
