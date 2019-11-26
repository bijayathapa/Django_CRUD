from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("all",views.all, name = 'all'),
    path("insert",views.insert),
    path("search_update",views.search_update),
    path("update",views.update),
    path("delete/<id>",views.delete),
]