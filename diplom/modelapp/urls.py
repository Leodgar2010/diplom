from django.urls import path
from .views import client_ifexist, add_client

urlpatterns = [
    path('client/<int:client_id>/', client_ifexist, name="client"),
    path ('client_form/', add_client, name = 'client_form'),
]