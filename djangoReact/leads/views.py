from rest_framework import generics
from leads.serializers import LeadSerializer
from leads.models import Lead

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
