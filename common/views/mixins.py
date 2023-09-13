from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ExtendGeneralViewSet(GenericViewSet):
    pass


class ListRetrieveViewSetMixin(ExtendGeneralViewSet, mixins.ListModelMixin,
                               mixins.RetrieveModelMixin):
    list_serializers = None
    retrieve_serializers = None

    def get_serializer_class(self):
        if self.action == 'list':
            return self.list_serializers
        if self.action == 'retrieve':
            return self.retrieve_serializers
        super().get_serializer_class()
