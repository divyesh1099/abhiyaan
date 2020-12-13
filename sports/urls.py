from django.urls import path
from . import views
app_name="sports"
urlpatterns=[
    path("", views.index, name="index"),
    path("indoor", views.isport, name="isport"),
    path("outdoor", views.osport, name="osport"),
    path("<str:sport>", views.sport, name="sport"),
]