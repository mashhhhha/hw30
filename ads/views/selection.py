from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import Selection
from ads.permissions import IsSelectionOwner
from ads.serializers import SelectionSerializer, SelectionCreateSerializer


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.all()
    default_serializer = SelectionSerializer
    serializer_classes = {
        'create': SelectionCreateSerializer,
    }

    default_permission = [AllowAny(), ]
    permissions_list = {"create": [IsAuthenticated()],
                        "update": [IsAuthenticated(), IsSelectionOwner()],
                        "partial_update": [IsAuthenticated(), IsSelectionOwner()],
                        "destroy": [IsAuthenticated(), IsSelectionOwner()]
                        }

    def get_permissions(self):
        return self.permissions_list.get(self.action, self.default_permission)

