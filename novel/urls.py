from django.urls import path

from novel import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("info/<int:pk>/", views.info, name="info"),
    path("edit/<int:pk>/", views.create, name="edit"),
    path("delete/<int:pk>/", views.delete, name="delete"),
]
