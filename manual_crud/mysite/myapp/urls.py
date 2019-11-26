from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("all", views.all, name='all'),
    path("get/<id>",views.getBook),
    path("insert",views.insert),
    path("search_update",views.getBookUpdate),
    path("update",views.updateBook),
    path("delete/<id>",views.deleteBook),
    
]