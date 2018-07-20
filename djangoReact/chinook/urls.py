from django.urls import path
from . import views
urlpatterns = [
    path('api/albums/', views.AlbumsListCreate.as_view() ),
]
