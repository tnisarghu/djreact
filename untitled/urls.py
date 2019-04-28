"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin

from django.urls import path, re_path, include # url
from .routers import router
from search.views import search_view
from books.views import (
    books_post_create_view,
)
from .views import (
    home_page,
    about_page,
    contact_page,
    example_page
)
from  django.views.generic import TemplateView

urlpatterns = [
    path('', home_page),
    path('admin/', admin.site.urls),  # it provides admin functionality
    path('admin/doc/', include('django.contrib.admindocs.urls')),  # provides admin doc functionality
    path('api/', include(router.urls)),
    path('learn/', include('learn.urls')),
    path('books/', include('books.urls')),
    path('search/', search_view),
    path('books-new/', books_post_create_view),
    path('page/', about_page),
    path('pages/', about_page),
    re_path(r'^pages?/$', about_page),
    re_path(r'^about/$', about_page),
    path('example/', example_page),
    path('contact/', contact_page),
]
#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
	
]

if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
