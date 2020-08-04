from django_mongoengine_filter import FilterSet, StringFilter
from vindecoder.models import Car


class CarFilter(FilterSet):
    wmi = StringFilter()
    country = StringFilter()

    class Meta:
        model = Car
        fields = ['wmi', 'country', 'mark']
