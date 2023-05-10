from django.views.generic import RedirectView
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from . import models
from . import serializers


class CreateShortURLApiView(generics.CreateAPIView):
    serializer_class = serializers.OriginalURLSErializer
    queryset = models.URL.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url = serializer.save()
        short_url = serializers.URLSerializer(instance=url, context={"request": request})
        return Response(data=short_url.data, status=status.HTTP_201_CREATED)


class ShortUrlRedirectView(RedirectView):
    def get_redirect_url(self, *args, short_url, **kwargs):
        url = get_object_or_404(models.URL, short_url=short_url)

        return url.url
