from django.urls import path
from web.views import index, subscriber


app_name = "web"

urlpatterns = [
    path("", index, name="index"),
    path("subscriber/", subscriber, name="subscriber")
]
