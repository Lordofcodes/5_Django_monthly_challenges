from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_challenges_by_numbers),
    path("january_1", views.january_1),  # the first ones are prioritized
    path("february_1", views.february_1),  # old versions
    path("<str:month>", views.monthly_challenges, name="month-challenge")  # place holder in brackets <>
]
