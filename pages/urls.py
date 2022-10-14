from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage, name="pages/homePage"),
    path('pages/',views.index,name="pages/index"),
    path('pages/about/',views.about,name="pages/about")
]
