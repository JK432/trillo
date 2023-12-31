from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..models import *
from django.conf import settings
from django_filters.rest_framework import FilterSet
from ..serializers import UserSerializer


class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = {
            'email': settings.FILTER_NUMBER_MODELS,
            'first_name': settings.FILTER_EXACT_MODELS,
            'last_name': settings.FILTER_EXACT_MODELS,
        }


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    filterset_class = UserFilter
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = User.objects.all()
        flag = self.request.query_params.get('flag', None)

        if flag is not None:
            queryset = User.objects.filter(id=self.request.user.id)

        return queryset



