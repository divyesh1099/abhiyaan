from django.urls import path
from . import views
app_name="maineventsdayone"
urlpatterns=[
    path("", views.index, name="index"),
    path("<str:event>", views.event, name="event"),
]