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
    path("update/add/prisoner/visitor/<int:prisoner_id>/", views.visitor_data, name="add_visitor"),
    path("update/add/prisoner/lawyer/<int:prisoner_id>/", views.lawyer_data, name="add_lawyer"),
    path("update/add/prisoner/court/<int:prisoner_id>/", views.court_data, name="add_court"),
    path("update/prisoner_select/", views.update_prisoner_select, name="update_prisoner_select"),
    path("update/prisoner_select/<int:prisoner_id>/", views.update_show_options, name="update_show_options"),
    path("update/prisoner_select/court/<int:prisoner_id>/", views.update_prisoner_court, name="update_prisoner_court"),
    path("update/prisoner_select/court/<int:prisoner_id>/<int:court_id>/", views.edit_update_prisoner_court, name="edit_update_prisoner_court"),
    path("update/prisoner_select/visitor/<int:prisoner_id>/", views.update_prisoner_visitor, name="update_prisoner_visitor"),
    path("update/prisoner_select/visitor/<int:prisoner_id>/<int:visitor_id>/", views.edit_update_prisoner_visitor, name="edit_update_prisoner_visitor"),
    path("update/prisoner_select/lawyer/<int:prisoner_id>/", views.update_prisoner_lawyer, name="update_prisoner_lawyer"),
    path("update/prisoner_select/lawyer/<int:prisoner_id>/<int:lawyer_id>/", views.edit_update_prisoner_lawyer, name="edit_update_prisoner_lawyer"),
    path("view/prisoner_select/", views.view_prisoner_select, name="view_prisoner_select"),
    path("view/prisoner_details/<int:prisoner_id>/", views.view_prisoner_details, name="view_prisoner_details"),
    path("view_database/", views.view_database, name="view_database_options"),
    path("view_database/view_courts/", views.view_courts, name="view_courts"),
    path("view_database/view_visitors/", views.view_visitors, name="view_visitors"),
    path("view_database/view_lawyers/", views.view_lawyers, name="view_lawyers"),
    path("view_database/search_by_filters/", views.search_by_filters, name="search_by_filters"),
    path("view_database/search_by_filters/search_by_cell/", views.search_by_cell, name="search_by_cell"),
    path("view_database/search_by_filters/search_by_crime/", views.search_by_crime, name="search_by_crime"),
    path("view_database/search_by_filters/search_by_gender/", views.search_by_gender, name="search_by_gender"),
    path("delete_prisoner_select/", views.delete_prisoner_select, name="delete_prisoner_select"),
    path("delete_prisoner_select/<int:prisoner_id>/", views.delete_and_show, name="delete_and_show"),
    path("view_database/view_all_prisoners/", views.view_all_prisoners, name="view_all_prisoners"),
    path("confirmation/", views.confirmation, name="confirmation"),
]