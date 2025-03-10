from django.urls import path

from portfolio import views, tag_views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.PortfolioCreateView.as_view(), name="create"),
    path("edit/<int:pk>/", views.PortfolioCreateView.as_view(), name="edit"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("delete/<int:pk>", views.DeletePortfolioView.as_view(), name="delete"),
    path("about/", views.about, name="about"),

    path("tag/", tag_views.index, name="tag"),
    path("tag/create/", tag_views.PortfolioTagCreateView.as_view(), name="tag_create"),
    path("tag/edit/<int:pk>/", tag_views.PortfolioTagCreateView.as_view(), name="tag_edit"),
    path("tag/delete/<int:pk>", tag_views.PortfolioTagDeleteView.as_view(), name="tag_delete"),
    path("tag/<int:tag_id>/", views.index, name="portfolio_by_tag"),
]