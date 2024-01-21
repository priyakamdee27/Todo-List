from django.urls import path
from . import views

urlpatterns = [
    path("add", views.add_item, name="add_item"),
    path("<int:id>/", views.add_item, name="update_item"),
    path("delete/<int:id>", views.delete_item, name="delete_item"),
    path("", views.item_list, name="item_list"),
]
