from django.urls import path
from .views import view_profile, edit_profile ,homepage

urlpatterns = [
    path('', homepage, name='homepage'),
    path('/templates/profiles/profile/', view_profile, name='view_profile'),
    path('/templates/profiles/edit_profile/', edit_profile, name='edit_profile'),
]
