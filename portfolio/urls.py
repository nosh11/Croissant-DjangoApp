from django.urls import path

from portfolio import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("edit/<int:pk>/", views.create, name="edit"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path('fetch-thumbnail/',views.fetch_thumbnail, name='fetch-thumbnail'),
]