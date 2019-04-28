from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BooksModelForm
from .models import Books
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def books_post_list_view(request):
    # list out objects 
    # could be search
    qs = Books.objects.all().published() # queryset -> list of python object
    if request.user.is_authenticated:
        my_qs = Books.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'books/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context) 


# @login_required
@staff_member_required
def books_post_create_view(request):
    # create objects
    # ? use a form
    # request.user -> return something
    form = BooksModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BooksModelForm()
    template_name = 'books/form.html'
    context = {'form': form}
    return render(request, template_name, context)  


def books_post_detail_view(request, slug):
    # 1 object -> detail view
    obj = get_object_or_404(Books, slug=slug)
    template_name = 'books/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)   

@staff_member_required
def books_post_update_view(request, slug):
    obj = get_object_or_404(Books, slug=slug)
    form = BooksModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'books/form.html'
    context = {"title": f"Update {obj.title}", "form": form}
    return render(request, template_name, context)  


@staff_member_required
def books_post_delete_view(request, slug):
    obj = get_object_or_404(Books, slug=slug)
    template_name = 'books/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/books")
    context = {"object": obj}
    return render(request, template_name, context)