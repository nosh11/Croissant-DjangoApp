from django.urls import path

from novel import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.NovelCreateView.as_view(), name="create"),
    path("info/<int:pk>/", views.NovelInfoView.as_view(), name="info"),
    path("edit/<int:pk>/", views.NovelCreateView.as_view(), name="edit"),
    path("delete/<int:pk>/", views.NovelDeleteView.as_view(), name="delete"),
]
