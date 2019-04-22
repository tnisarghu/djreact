# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from django.utils import timezone
from .models import Learn


class IndexView(generic.ListView):
    template_name = 'learn/index.html'
    context_object_name = 'latest_learn_list'
	latest_subject_list = ["Anatomy", "Physiology", "Bioochemistry"]
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Learn.objects.filter(
        pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Learn
    template_name = 'learn/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Learn.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    latest_subject_list = ["Anatomy", "Physiology", "Bioochemistry"]
    template_name = 'learn/base.html'

def vote(request, learn_id):
    return HttpResponse("You're voting on question %s." % learn_id)