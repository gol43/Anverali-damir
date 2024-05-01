from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.view_or_edit_profile, name='view_profile'),
    path('profile/create/', views.create_profile, name='create_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
