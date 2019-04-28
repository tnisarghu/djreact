from django.shortcuts import render
from books.models import Books
from .models import SearchQuery

# Create your views here.


def search_view(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context =  {"query": query}
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        books_list = Books.objects.search(query=query)
        context['books_list'] = books_list
    return render(request, 'search/view.html',context)