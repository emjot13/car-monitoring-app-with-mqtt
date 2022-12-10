from django.urls import path
from . import views

app_name = "web_client"

urlpatterns = [
    path('', views.start, name="start"),
    path("add_car", views.add_car_form, name="add_car_form"),
    path("add_car_to_database", views.add_car, name="add_car"),
    path("check_car", views.check_car, name="check_car"),
    path("check_car_form", views.check_car_form, name="check_car_form"),

]