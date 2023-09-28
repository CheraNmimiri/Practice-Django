from django.urls import path

from . import views


urlpatterns = [
    path("", views.register, name='register'),
    path("validate", views.validate, name='validate'),
    path("login", views.login, name='login'),
    path("successfull" , views.check, name="check"),
]
