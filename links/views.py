from rest_framework import generics

from links.models import Link
from links.serializers import LinkSerialezer


class LinkListCreate(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerialezer