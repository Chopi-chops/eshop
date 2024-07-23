from .models import New
import django_filters


class NewFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Название"
    )
    article = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Содержание"
    )
    views__gte = django_filters.NumberFilter(
        field_name='views',
        lookup_expr="gte",
        label="Просмотры, от"
    )
    views__lte = django_filters.NumberFilter(
        field_name='views',
        lookup_expr="lte",
        label="Просмотры, до"
    )

    class Meta:
        model = New
        fields = [
            'title', 'article',
            'views__gte', 'views__lte',
            'category',
        ]
