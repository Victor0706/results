from django_filters import FilterSet, DateTimeFilter, ModelMultipleChoiceFilter
from django.forms import DateTimeInput
from .models import Response


class ResponseFilter(FilterSet):
    class Meta:
       model = Response
       fields = {
           'article': ['exact'],
       }
