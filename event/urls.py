from django.urls import path
from event.views import show_event, create_event, edit_event

app_name = "event"

urlpatterns = [
    path("", show_event, name="show_event"),
    path("create", create_event, name="create_event"),
    path("edit/<uuid:id>", edit_event, name="edit_event"),
]