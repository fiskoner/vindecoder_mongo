# -*- coding: utf-8 -*-
import os

from django.http import JsonResponse
from vindecoder.models import Car
from vindecoder.serializers import CarSerializer
from rest_framework_mongoengine.generics import ListAPIView
from rest_framework_csv.renderers import CSVRenderer
from rest_framework.settings import api_settings
from vindecoder.filters import CarFilter


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    serializer = JsonResponse
    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES) + (CSVRenderer,)

    def filter_queryset(self, queryset):
        filter = CarFilter(self.request.query_params, queryset=queryset)
        return filter.qs

    def _generate_filename(self):
        wmi = self.kwargs.get('key', None)
        return f'wmicsv_{wmi}'

    def finalize_response(self, request, response, *args, **kwargs):
        if response.status_code == 200 and self.request.query_params.get('format', None) == 'csv':
            response['Content-Disposition'] = f'attachment;filename={self._generate_filename()}.csv'
        return super(CarListView, self).finalize_response(request, response, *args, **kwargs)