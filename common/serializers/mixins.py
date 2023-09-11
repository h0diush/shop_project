from rest_framework import serializers


class ExtendModelSerializers(serializers.ModelSerializer):
    """
    Миксин сериализатора
    """

    class Meta:
        abstract = True


class ListModelSerializersMixin(ExtendModelSerializers):
    slug = serializers.SerializerMethodField()

    def get_slug(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.slug)
        return None
