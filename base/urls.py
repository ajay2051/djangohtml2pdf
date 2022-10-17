from django.urls import path
from .views import GeneratePdf


urlpatterns = [
path('', GeneratePdf.as_view()),
]