from rest_framework.viewsets import ModelViewSet

from ads.models import Selection
from ads.serializers import SelectionSerializer


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer