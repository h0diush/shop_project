from rest_framework import serializers


class ExtendModelSerializers(serializers.ModelSerializer):
    """
    Миксин сериализатора
    """

    class Meta:
        abstract = True


class ListModelSerializersMixin(ExtendModelSerializers):
    pass
