from django.urls import path
from catalog.apps import CatalogConfig
# from catalog.views import home
# from catalog.views import contacts
from catalog.views import index


app_name = CatalogConfig.name

# urlpatterns = [
#     path("", home, name="home"),
#     path("contacts/", contacts, name="contacts"),
# ]

urlpatterns = [
    path("", index)
]