from django.urls import path
from . import views

#path should start with it --> v1/
urlpatterns = [
    path("", views.index, name="index"),
    #path("base/", views.generic, name="generic")
    path("update/add/prisoner/", views.prisoner_data, name="prisoner_data"),
    path("update/", views.update_or_add, name="update_or_add"),
    path("update/details/", views.add_prisoner_details, name="prisoner_details"),
    path("update/prisoner/", views.select_prisoner, name="select_prisoner"),
    path("update/prisoner/<int:prisoner_id>/", views.prisoner_details_boxes, name="prisoner_details_boxes"),
    path("update/add/prisoner/crime/<int:prisoner_id>/", views.crime_data, name="add_crime_fir"),
    path("update/add/prisoner/court/<int:prisoner_id>/", views.court_data, name="add_court"),
    path("update/prisoner_select/", views.update_prisoner_select, name="update_prisoner_select"),
    path("update/prisoner_select/<int:prisoner_id>/", views.update_show_options, name="update_show_options"),
    path("update/prisoner_select/court/<int:prisoner_id>/", views.update_prisoner_court, name="update_prisoner_court"),
    path("update/prisoner_select/court/<int:prisoner_id>/<int:court_id>/", views.edit_update_prisoner_court, name="edit_update_prisoner_court"),
]