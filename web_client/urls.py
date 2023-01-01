from django.urls import path
from . import views

app_name = "web_client"

urlpatterns = [
    path('', views.start_page, name="start_page"),
    path('login', views.login, name="login"),

    path("register", views.register, name="register"),
    path("start", views.start, name="start"),
    path("add_car", views.add_car_form, name="add_car_form"),
    path("add_car_to_database", views.add_car, name="add_car"),
    path("check_car", views.check_car, name="check_car"),
    # path("check_car_form", views.check_car_form, name="check_car_form"),
    path("see_car_status", views.see_car_status, name="see_car_status"),
    path("see_my_cars", views.see_my_cars, name="see_my_cars"),
    path("delete_car", views.delete_car, name="delete_car"),
    path("update_car_form", views.update_car_form, name="update_car_form"),
    path("update_car", views.update_car, name="update_car"),

]