from rest_framework import serializers

from links.models import Link


class LinkSerialezer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['title', 'url']