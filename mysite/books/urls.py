from django.urls import path

from . import views


urlpatterns = [
    path("", views.index),
    path("horoscope/type", views.index1),
    path("<int:sign_zodiac>", views.get_info_about_sign_zodiac_by_number),
    path("<str:sign_zodiac>", views.get_info_about_sign_zodiac, name='horoscope-name'),
    path("horoscope/type/<str:und>", views.get_info_style, name='type'),
    path("horoscope/<str:month>/<int:day>", views.get_info_by_date)
]