from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_listing, name="product_list"),
    path(
        "<slug:category_slug>/", views.product_listing, name="product_list_by_category"
    ),
    path(
        "<slug:category_slug>/<slug:product_slug>/",
        views.product_detail,
        name="product_detail",
    ),
    path(
        "<slug:category_slug>/<slug:product_slug>/",
        views.product_review,
        name="product_review",
    ),
]
