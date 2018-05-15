from .models import Document,Advertise
import django_filters

class DocumentFilter(django_filters.FilterSet):
    class Meta:
        model = Document
        fields = {'title':['icontains'], 'genre':['icontains'], 'author':['icontains'], }


class AdvertiseFilter(django_filters.FilterSet):
    class Meta:
        model = Advertise
        fields = {'title':['icontains'], 'genre':['icontains'], 'author':['icontains'], }
