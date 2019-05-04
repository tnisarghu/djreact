# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from .models import Learn


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'learn/index.html'
    context_object_name = 'latest_learn_list'
    """
         :view:'learn.IndexView'   Return the last five published questions (not including those set to be
            published in the future).
    """
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Learn.objects.all()


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Learn
    template_name = 'learn/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Learn.objects.all()


class BaseView(generic.DetailView):
    model = Learn
    template_name = 'base.html'

def vote(request, learn_id):
    return HttpResponse("You're voting on question %s." % learn_id)
"""  class Library(generic.DetailView):
	model = LearnName
    template_name = 'learn/library.html'

	def get_queryset(self):

        return LearnName.objects.filter(pub_date__lte=timezone.now())
        """


def library(request):
    obj = Learn.objects.all()
    template_name = 'learn/library.html'
    # context = {"title": [obj.name], "subject": [obj.subject], "main_topic": [obj.main_topic], "sub_topic": [obj.sub_topic]
    context = {'obj': obj}
    return render(request, template_name, context)