from django.urls import path

from . import views
app_name = "usuarios"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("registro/", views.registro, name="registro"),
]