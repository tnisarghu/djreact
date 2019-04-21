from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic


from .models import Learn


class IndexView(generic.ListView):
    template_name = 'learn/index.html'
    context_object_name = 'latest_learn_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Learn.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Learn
    template_name = 'learn/detail.html'


class ResultsView(generic.DetailView):
    model = Learn
    template_name = 'learn/results.html'

def vote(request, learn_id):
    return HttpResponse("You're voting on question %s." % learn_id)