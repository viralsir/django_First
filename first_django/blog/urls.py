from django.urls import path
from .views import view_post,view_json_post
urlpatterns=[
    path("view/",view_post,name="view"),
    path("jsonview/",view_json_post,name="viewjson")
]