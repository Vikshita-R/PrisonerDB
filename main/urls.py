from django.urls import path
from . import views

#path should start with it --> v1/
urlpatterns = [
    path("", views.index, name="index"),
    #path("base/", views.generic, name="generic")
    path("update/prisoner/add/", views.prisoner_data, name="prisoner_data"),
    path("update/", views.update_or_add, name="update_or_add"),
]