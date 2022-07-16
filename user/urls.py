from . views import (ProductListView,ProductAddView,
                            CartItemDisplayView,EditCartProductView,CartItemAdded,
                            CartItemRemove,EmptyCartView)
from django.urls import path,include


urlpatterns = [
    path("product-list/",ProductListView.as_view(),name="product_list"),
    path("product-add/<int:id>/",ProductAddView.as_view(),name="product_add"),
    path("cart/",CartItemDisplayView.as_view(),name="cart_display"),
    path("product-edit/<int:id>/",EditCartProductView.as_view(),name="product_edit"),
    path("cart-add/<int:id>/",CartItemAdded.as_view(),name="cart_add"),
    path("cart-remove/<int:id>/",CartItemRemove.as_view(),name="cart_remove"),
    path("empty/",EmptyCartView.as_view(),name="cart_empty"),

]