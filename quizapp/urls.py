from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("maliyo-admin/", admin.site.urls),
    path("", include("quiz.urls", "quiz")),
    path("newquiz/", include("newquiz.urls")),
]
