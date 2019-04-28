from django.urls import path
# from . import views
from .views import (
    books_post_detail_view,
    books_post_list_view,
    books_post_update_view,
    books_post_delete_view,
)


app_name = 'books'
urlpatterns = [
    path('', books_post_list_view, name='index'),
    path('<str:slug>/', books_post_detail_view, name='detail'),
    path('<str:slug>/edit/', books_post_update_view, name='update'),
    path('<str:slug>/delete/', books_post_delete_view, name='delete'),
]