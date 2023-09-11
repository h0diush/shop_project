from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework import mixins


class ExtendGeneralViewSet(GenericViewSet):
    pass


class ListViewSetMixin(ExtendGeneralViewSet, mixins.ListModelMixin,
                       mixins.RetrieveModelMixin):
    pass

    lookup_field = 'slug'
