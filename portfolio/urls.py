from django.urls import path

from portfolio import views, tag_views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("edit/<int:pk>/", views.create, name="edit"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path('fetch-thumbnail/',views.fetch_thumbnail, name='fetch-thumbnail'),
    path("tag/", tag_views.index, name="tag"),
    path("tag/create/", tag_views.create, name="tag_create"),
    path("tag/edit/<int:pk>/", tag_views.create, name="tag_edit"),
    path("tag/delete/<int:pk>", tag_views.delete, name="tag_delete"),
]