from django.urls import path

from . import views

app_name = 'learn'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/base/', views.BaseView.as_view(), name='base'),
    # ex: /polls/5/vote/
    path('<int:learn_id>/vote/', views.vote, name='vote'),
	# path('<int:learn_id>/library/', views.Library.as_view(), name='index'),
]