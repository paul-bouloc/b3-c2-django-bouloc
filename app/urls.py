from django.urls import include, path

from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("add/", views.add, name="add"),
    path("add/submit", views.addSubmit, name="addSubmit"),
    path("detail/<int:id>", views.detail, name="detail"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("edit/submit/<int:id>", views.editSubmit, name="editSubmit"),
    # path("delete/<int:id>", views.delete, name="delete"),
]