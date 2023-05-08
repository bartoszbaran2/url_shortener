from rest_framework import serializers

from .models import URL


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ("id", "short_url")


class OriginalURLSErializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ("url",)
