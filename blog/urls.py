from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blog"),
    path("posts/", views.posts, name="posts"),
    path("posts/<slug:details>", views.post_details,name="post_details")
]
