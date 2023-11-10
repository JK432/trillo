from rest_framework.viewsets import ModelViewSet
from ..models import *
from ..serializers import *
from django.conf import settings
from django_filters.rest_framework import FilterSet
from ..mixins.user_mixin import Role
from rest_framework.permissions import IsAuthenticated


class TicketFilter(FilterSet):
    class Meta:
        model = Ticket
        fields = {
            'title': settings.FILTER_STRING_MODELS,
            'created_time': settings.FILTER_TIME_MODELS,
            'assignee': settings.FILTER_EXACT_MODELS,
            'created_by': settings.FILTER_EXACT_MODELS,
            'Status': settings.FILTER_EXACT_MODELS,
        }


class TicketViewSet(ModelViewSet):
    serializer_class = TicketSerializer
    filterset_class = TicketFilter
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # if self.request.user.role == Role.DEV:
        #     return Ticket.objects.filter(user__role=Role.DEV, assignee=self.request.user)
        # else:
            return Ticket.objects.all()

# FILTER_STRING_MODELS = ['exact', 'icontains', 'istartswith', 'iendswith']
# FILTER_NUMBER_MODELS = ['exact', 'lt', 'lte', 'gt', 'gte']
# FILTER_EXACT_MODELS = ['exact']
# FILTER_TIME_MODELS = ['exact', 'year', 'month', 'day', 'hour', 'minute', 'second', 'range']
