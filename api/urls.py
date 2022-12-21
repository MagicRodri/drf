from django.urls import path
from rest_framework.schemas import get_schema_view

from .views import EntityList

schema_view = get_schema_view(
    title='API title',
    description='API description',
    version='1.0.0',
)

urlpatterns = [
    path('', schema_view, name='openapi-schema'),
    path('entities/', EntityList.as_view()),
]