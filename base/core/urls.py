from django.urls import path, re_path
from core.views import home, createurl, retrieve

urlpatterns = [
    path('', home, name='home'),
    path('createurl/', createurl, name='createurl'),
    re_path(r'^(?P<input_url>[0-9a-zA-Z]+)/$', retrieve, name='retrieve'),
]