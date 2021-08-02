from django.urls import path
from django.contrib import admin
from encyclopedia.views import index
from encyclopedia.views import entry
from encyclopedia.views import search
from encyclopedia.views import create
from encyclopedia.views import rnd
from encyclopedia.views import edit


from . import views


urlpatterns = [
    path("", index, name="index"),
    path('wiki/<str:entry>',entry,name="entry"),
    path("search",search,name="search"),
    path("create",create,name="create"),
    path("rnd",rnd,name="rnd"),
    path("wiki/edit/<str:title>",edit,name="edit"),
]
