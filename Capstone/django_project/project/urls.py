from django.urls import path
from django.urls.resolvers import URLPattern

from .import views

urlpatterns = [ 
path("", views.index, name="index"),
path("register/", views.register, name="register"),
path("contacts/add_contact/", views.add_contact),
path("contacts/delete_contact/<int:id>/", views.delete_contact),
path("contacts/register", views.register, name="register"),
path("register/register", views.register, name="register"),
path("contacts/", views.contacts, name="contacts"),
path("login/", views.login, name="login"),
path("search/", views.search, name="search"),
path("login/login", views.login, name="login"),
path("logout/", views.logout, name="logout"),
path("contacts/logout/", views.logout, name="logout"),
path("contacts/search/logout/", views.logout, name="logout"),
path("search/contacts/logout/", views.logout, name="logout"),
path("contacts/search/", views.search, name="search"),
path("search/contacts/", views.contacts, name="contacts"),
path("search/contacts/delete_contact/<int:id>/", views.delete_contact),
]