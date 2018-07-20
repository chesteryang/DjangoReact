from rest_framework import generics
from chinook.serializers import AlbumsSerializer
from chinook.models import Albums

class AlbumsListCreate(generics.ListCreateAPIView):
    queryset = Albums.objects.all()
    serializer_class = AlbumsSerializer
