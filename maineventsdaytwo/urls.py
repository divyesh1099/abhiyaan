from django.urls import path
from . import views
app_name="maineventsdaytwo"
urlpatterns=[
    path("", views.index, name="index"),
    path("<str:event>", views.event, name="event"),
]