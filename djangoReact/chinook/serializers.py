from rest_framework import serializers
from chinook.models import Albums

class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = '__all__'
