from django.urls import path

from .views import EntityList

urlpatterns = [
    path('entities/', EntityList.as_view()),
]