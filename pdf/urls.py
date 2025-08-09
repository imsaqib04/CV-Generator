from django.contrib import admin
from django.urls import path,include

from .views import ProfileListCreateView,generate_pdf_view

urlpatterns = [
    path('profiles/',ProfileListCreateView.as_view(),name="profile-list-create"),
    path('profiles/<int:pk>/pdf/', generate_pdf_view, name='generate-pdf'),
]

