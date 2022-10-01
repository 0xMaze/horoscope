from django.urls import path

from . import views

app_name = "horoscope"
urlpatterns = [
    path("", views.index, name="index"),
    path("your_horoscope/", views.horoscope, name="horoscope_page"),
]
