from django.urls import path

from portfolio import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("detail/<int:pk>/", views.detail, name="detail"),
]