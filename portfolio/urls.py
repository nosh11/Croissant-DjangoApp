from django.urls import path

from portfolio import views, tag_views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.PortfolioCreateView.as_view(), name="create"),
    path("edit/<int:pk>/", views.PortfolioCreateView.as_view(), name="edit"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("tag/", tag_views.index, name="tag"),
    path("tag/create/", tag_views.create, name="tag_create"),
    path("tag/edit/<int:pk>/", tag_views.create, name="tag_edit"),
    path("tag/delete/<int:pk>", tag_views.delete, name="tag_delete"),
    path("tag/<int:tag_id>/", views.index, name="portfolio_by_tag"),
]